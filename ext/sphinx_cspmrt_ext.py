from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective

import os
import time

#目录节点
class bloglist(nodes.General, nodes.Element):
    pass

#元数据节点
class metadatanode(nodes.Admonition, nodes.Element):
    pass

def visit_metadata_node(self, node):
    self.visit_admonition(node)


def depart_metadata_node(self, node):
    self.depart_admonition(node)

class metaDirective(SphinxDirective):

    # this enables content in the directive
    has_content = True 

    def run(self):
        
        #如果不存在则创建
        if not hasattr(self.env, 'blog_all_list'):
            self.env.blog_all_list = {}
            self.env.time_list = []

        time_data = time.strptime(self.content[1], "%Y,%m,%d")  #获取时间
        time_stamp = int(time.mktime(time_data))

        metastr_author = "作者：" + self.content[0]
        metastr_date = "创建时间：" + str(time_data.tm_year) + "年" + str(time_data.tm_mon) + "月" + str(time_data.tm_mday) +"日"

        #如果时间重复则时间戳+1
        while str(time_stamp) in self.env.blog_all_list:
            time_stamp += 1

        self.env.time_list.append(time_stamp)
        self.env.blog_all_list[str(time_stamp)] = {
            'docname': self.env.docname,
            'data' : metastr_author + '    ' + metastr_date
        }

        print(self.content,'    ',self.env.docname,'    ')

        node = metadatanode()
        node += nodes.title(_("文档元数据"), _("文档元数据"))
        node += nodes.paragraph(_(metastr_author), _(metastr_author))
        node += nodes.paragraph(_(metastr_date), _(metastr_date))
        print(node)
        return [node]


class bloglistDirective(Directive):

    def run(self):
        return [bloglist('')]

#当文件被修改时，清理过期项
def purge_list(app, env, docname):
    if not hasattr(env, 'time_list'):
        return
    
    env.time_list = [l for l in env.time_list
                            if env.blog_all_list[str(l)]['docname'] != docname]

#判断sub是否属于main同一目录或子目录
def samepath(main, sub):
    maindir = os.path.split(main)[0]
    subdir = os.path.split(sub)[0]
    print(maindir,'====',subdir,' ',os.path.commonprefix([maindir, subdir]))
    if os.path.commonprefix([maindir, subdir]) == maindir:
        return True
    else:
        return False

#获取标题
def get_title(env, docname):
    title = env.titles[docname]
    title = str(title)
    #除掉<title>
    if title.find('<title>') == 0:
        title = title[7:-8]
    
    return title

#处理数据
def process_meta_nodes(app, doctree, fromdocname):
    env = app.builder.env
    print(env.time_list)
    env.time_list.sort(reverse=True)    #对时间进行倒序排序
    for node in doctree.traverse(bloglist):
        content = []
        for time_list in env.time_list:
            blog_list = env.blog_all_list[str(time_list)]
            #判断是否是同一层目录
            if not samepath(fromdocname, blog_list['docname']):
                continue

            para = nodes.paragraph()
            ref = nodes.reference('','')
            innernode = nodes.emphasis(get_title(env, blog_list['docname']), get_title(env, blog_list['docname']))
            ref['refdocname'] = blog_list['docname']
            ref['refuri'] = app.builder.get_relative_uri(
                fromdocname, blog_list['docname']
            )
            ref.append(innernode)
            para += ref
            em = nodes.generated()
            em += nodes.emphasis('   '+blog_list['data'], '    '+blog_list['data'])
            #para.append(em)
            print(para)
            content.append(para)
        
        node.replace_self(content)

def setup(app):
    app.add_node(bloglist)
    app.add_node(metadatanode,
                html=(visit_metadata_node, depart_metadata_node),
                latex=(visit_metadata_node, depart_metadata_node),
                text=(visit_metadata_node, depart_metadata_node))

    app.add_directive('metadata', metaDirective)
    app.add_directive('bloglist', bloglistDirective)
    app.connect('doctree-resolved', process_meta_nodes)
    app.connect('env-purge-doc', purge_list)
    
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
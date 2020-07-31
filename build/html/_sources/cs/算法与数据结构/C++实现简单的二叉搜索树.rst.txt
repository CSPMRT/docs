*************************
C++实现简单的二叉搜索树
*************************

.. note:: 
   作者：Chen Longhao   时间：2020年7月23日

.. warning::
   这是一个演示程序，没有经过充分测试，请不要用于生产环境

.. code-block:: cpp
   
   #include <iostream>
   using namespace std;

   //树节点
   struct node{
      node *left = NULL;
      node *right = NULL;
      int data;
   };

   class tree{
      node *HEAD = NULL;
      node *p;
      public:
      //添加数据
      void add(int data){
         //如果头节点为空，则创建头节点
         if(HEAD == NULL){
            HEAD = new node;
            HEAD->data = data;
         }else{
            p = HEAD;
            while(true){
               //大于保存到右节点，否则保存到左节点
               if(data > p->data){
                  if(p->right == NULL){
                     p->right = new node;
                     p->right->data = data;
                     break;
                  }else
                     p = p->right;
               }else{
                  if(p->left == NULL){
                     p->left = new node;
                     p->left->data = data;
                     break;
                  }else
                     p = p->left;
               }
            }
         }
      }

      //判断数据是否存在
      bool exist(int data){
         p = HEAD;
         while(p != NULL){
            if(p->data == data)
               return true;
            if(data > p->data)
               p = p->right;
            else
               p = p->left;
         }
         return false;
      }

      //获取最小值
      int getmin(){
         p = HEAD;
         while(p->left != NULL)
            p = p->left;
         return p->data;
      }

      //获取最大值
      int getmax(){
         p = HEAD;
         while(p->right != NULL)
            p = p->right;
         return p->data;
      }
   };

   //以下为测试代码
   int pd(bool data){
      if(data){
         cout << "true" << endl;
      }else{
         cout << "false" << endl;
      }
      return 0;
   }

   int main(){
      tree a;
      a.add(1);
      a.add(3);
      a.add(2);
      a.add(0);
      a.add(-56);
      pd(a.exist(7));
      pd(a.exist(2));
      pd(a.exist(1));
      pd(a.exist(0));
      cout << a.getmax() << "\t" << a.getmin() << endl;
   }


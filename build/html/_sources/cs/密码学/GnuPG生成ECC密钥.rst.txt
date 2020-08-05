******************
GnuPG生成ECC密钥
******************

.. metadata::
   Chen Longhao
   2020,07,05

GnuPG简介
-----------
GNU Privacy Guard（GnuPG或GPG）是一种加密软件，它是PGP加密软件的满足GPL的替代物。
GnuPG依照由IETF订定的OpenPGP技术标准设计。GnuPG用于加密、数字签名及产生非对称钥匙对的软件。
具体简介可以看：https://baike.baidu.com/item/GnuPG

如果你想尝试其中的一些功能，可以试试我开发的网页版的完全兼容GnuPG的加密程序OpenPGP-Web：https://chenlhlinux.github.io/pgpweb/

ECC简介
--------
ECC是椭圆曲线密码学的缩写，一种建立公开密钥加密的演算法，基于椭圆曲线数学。椭圆曲线在密码学中的使用是在1985年由Neal Koblitz和Victor Miller分别独立提出的。
ECC的主要优势是在某些情况下它比其他的方法使用更小的密钥——比如RSA加密算法——提供相当的或更高等级的安全。
具体简介可以看：https://baike.baidu.com/item/%E6%A4%AD%E5%9C%86%E5%8A%A0%E5%AF%86%E7%AE%97%E6%B3%95/10305582

算法原理可以看：https://zhuanlan.zhihu.com/p/36326221

GnuPG生成ECC密钥
------------------
因为ECC是一种比较新的算法，在gpg默认的密钥生成菜单中并不包含ECC密钥，如果需要生成ECC密钥，
则需要启用专家模式。

执行命令：``gpg --full-gen-key --expert``

会返回:

.. code-block::

   gpg (GnuPG) 2.2.12; Copyright (C) 2018 Free Software Foundation, Inc.
   This is free software: you are free to change and redistribute it.
   There is NO WARRANTY, to the extent permitted by law.

   请选择您要使用的密钥类型：
      (1) RSA 和 RSA （默认）
      (2) DSA 和 Elgamal
      (3) DSA（仅用于签名）
      (4) RSA（仅用于签名）
      (7) DSA（自定义用途）
      (8) RSA（自定义用途）
      (9) ECC 和 ECC
   (10) ECC（仅用于签名）
   (11) ECC（自定义用途）
   (13) 现存的密钥
   您的选择是？

9,10,11即为生成ECC密钥。我们选择 ``(9) ECC 和 ECC``

然后就会进入曲线选择菜单

.. code-block::

   请选择您想要使用的椭圆曲线：
      (1) Curve 25519
      (3) NIST P-256
      (4) NIST P-384
      (5) NIST P-521
      (6) Brainpool P-256
      (7) Brainpool P-384
      (8) Brainpool P-512
      (9) secp256k1
   您的选择是？

这里我推荐使用 ``(1) Curve 25519`` 

.. note::
   关于Curve 25519可以参见：https://www.zhihu.com/question/290541183/answer/529676502

接下来就和创建普通RSA密钥差不多，按照说明去填即可。

cd D:/MyGit   ��λ��git���ַ
git config --global user.name "Your Name" �����û���
git config --global user.email "email@example.com"  ����email

pwd  ��ѯ��ǰ·��
mkdir projectname  �½��ļ��У����汾��
cd projectname ��λ����Ŀ�ļ���
git init    �ڵ�ǰ·���´�������ʼ��Git �ֿ⣬��Ÿ���Ŀ����������
�����Ƚ�git add���ݴ���������git commit���汾����ȥ
git add filename  �ύ����/�޸ĵ��ļ����ݴ���
git commit -m "explanation about what you add"  �������/�޸ĵ��ļ����ݴ����ύ����֧�⣬��������ݴ���
git status   �鿴�ֿ⵱ǰ״̬�����ļ����޸ĵ�
git diff  ��ʾ�ļ��޸ĵľ�������
git log  �鿴�޸ļ�¼
cat filename  �鿴�ļ�����
git reflog �鿴ÿ��ִ�е�����
git checkout -- filename    ���ļ��ص����һ��git commit��git addʱ��״̬,��������ȥ���޸�
git reset HEAD filename    ���ݴ������޸Ļ��˵�������
���˰汾��
HEAD����ǰ�汾  
git reset --hard HEAD^   ���˵���һ���汾
git reset --hard HEAD~100 ���˵���100���汾
git reset --hard commit_id       ����/���ص���Ӧ�汾(be68Ϊcommit id)
rm filename  ɾ�����������ļ�
git rm filename ɾ���汾���е��ļ�
git checkout -- filename ʹ�ð汾���еİ汾�滻�������İ汾�������汾���е��ļ��ָ�����������

***********************MyGit ������
***********************.gitΪ�汾��
һ���޸ĵ�����:Git add->���ļ���ӵ��汾����ݴ���--->Git commit�ύ���汾���master��֧

ssh-keygen -t rsa -C "email"   ����SSH����
git remote add origin git@github.com:username/filename.git   �����ؿ������github�Ŀ����������Ҫ�ڱ��ؿ�·��������
git push -u origin master             �����ؿ�������������͵�Զ�̿���ȥ���״�ָ��Ĭ�Ϸ���������Ҫ���-u
ssh -T git@github.com                                          git����github
git clone git@github.com:username/projectname��¡Զ�̿⵽���ؿ���
ls �鿴��ǰ·���µ��ļ���



�½���֧�����л�����֧
���������޸ĵ����ݸ��µ���֧��������ʱmaster��֧���ݱ��ֲ���
��dev�������ɣ���ȷ��������л���master��֧�����ϲ�dev��֧����ʱ���߿����ͬ����״̬
��֧����
git checkout -b dev    ������Ϊdev�ķ�֧(-b��ʾ�������л�)
= git branch dev  +  git checkout dev   ������֧dev + �л���֧

git branch �鿴��ǰ��֧
git checkout master  �л�Ϊmaster��֧���л���֧ǰȷ���ѽ����������ݸ��µ�git����ȥ
git log ��ʾ Endʱ������CTRL+C or ����q��
git merge  --no-ff -m ��explanation��  dev  
��ָ����dev��֧�ϲ�����ǰ��֧(��master��֧)��ȥ���������ͬ��
git branch -d dev ɾ��dev��֧
git branch -D dev ǿ��ɾ��dev��֧
git log --graph   �ɲ鿴��֧�ϲ�ͼ
<<<<<<< HEAD
=======
git log --graph --pretty=oneline --abbrev-commit   �鿴��֧�ϲ�ͼ
>>>>>>> dev
branch test1 and test2
git stash ����ǰ�����ֳ��������������������ָ��ټ�����һ��������ʱ�½���֧ȥ��bug
git stash list �鿴����Ĺ����ֳ�
git stash pop = git stash apply + git stash drop �ָ���ɾ��stash
<<<<<<< HEAD
git stash apply stash@{0} ѡ��ָ����stash�ָ�
=======
git stash apply stash@{0} ѡ��ָ����stash�ָ�

git remote �鿴Զ�̿�
git remote -v �鿴ץȡ�����͵�origin�ĵ�ַ�����û������Ȩ�ޣ��Ϳ�����push�ĵ�ַ

����Э���Ĺ���ģʽͨ����������

    1.���ȣ�������ͼ��git push origin <branch-name>�����Լ����޸ģ�

    2.�������ʧ�ܣ�����ΪԶ�̷�֧����ı��ظ��£���Ҫ����git pull��ͼ�ϲ���

    3.����ϲ��г�ͻ��������ͻ�����ڱ����ύ��

    4.û�г�ͻ���߽������ͻ������git push origin <branch-name>���;��ܳɹ���

���git pull��ʾno tracking information����˵�����ط�֧��Զ�̷�֧�����ӹ�ϵû�д�����������git branch --set-upstream-to <branch-name> origin/<branch-name>��
>>>>>>> dev

git tag v1.0 �ڵ�ǰ��֧����±�ǩ
git tag �鿴���б�ǩ
git tag -d v1.0ɾ����ǩ
git push origin v1.0���ͱ�ǩ��Զ�̿�
git push origin --tags  �������б�ǩ��Զ�̿�
git push origin :refs/tags/v1.0ɾ��Զ�̵ı�ǩ
git show v1.0 �鿴��ǩ�ľ�����Ϣ
git tag v1.1  commit_id ��Դ˴ε�commit���tag
git tag -a v1.2 -m "version 1.2 released" commit_id��Ӵ���˵���ı�ǩ��-aָ����ǩ����-mָ��˵������

���������͵�Զ�̿���ȥ
git push master  #���͵�Զ�̿��master����֧
git push dev     #���͵�Զ�̿�Ķ�Ӧ��֧��


Gitee #����
git remote add origin_gitee git@gitee.com:Arlen/python.git #git���ӵ����Ƶ�Զ�̿�
git push origin_gitee master
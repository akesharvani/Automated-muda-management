# About this project

This project was made to automatically Post Blogs on muda management through a docx file.

There are two modes to do so 

- <a href="#method1">Method 1: Using API</a>
- <a href="#method2">Method 2: Using Browser and GUI</a>

# Preparing Docs File:

To prepare docx file to be automated simply add keyword 'EOT' at the end of every title and 'EOB' at the end of every blog.
That's it! Now follow any of the methods below to automate the process and watch your Rocket fly!

# <a id ="method1"></a> Method 1: Using API

This is easier to do than GUI as it requires only few changes in the code:
 - Comment line number 99 : 'automate_via_gui()'
 - Uncomment line number 100 : 'automate_via_api()'

 Thats it. Now press ctrl+shift+p and enter 'Run Robot' and watch all your blogs get posted on muda management.

 ## Additional changes

 If you want to change default Author_id and Category_id of the blogs then change the values of 'author' and 'category' in line number 72 and 73 respectively.

 <b>Note : </b> Remember this id will be used for all the blogs in the docx file. and can not be changed for individual blogs.


# <a id ="method2"></a> Method 2: Using GUI or Browser

This is a little trickier to do than API as it requires changing database code of Muda Management.:
 - Change RichTextField in muda management models.py file to TextField (This might cause some issues in production so only do this in development environment)
 - Uncomment line number 99 : 'automate_via_gui()'
 - Comment line number 100 : 'automate_via_api()'
 - Change line 32,33 username and password to your muda management username and password for admin control.

 Thats it. Now press ctrl+shift+p and enter 'Run Robot' and watch all your blogs get posted on muda management.

 ## Additional changes

 If you want to change default Author_id and Category_id of the blogs then change the values of 'author' and 'category' in line number 34 and 35 respectively.

 <b>Note : </b> Remember this id will be used for all the blogs in the docx file. and can not be changed for individual blogs.



# Template: Standard Robot Framework

This is the simplest template to start from.

- Get started from a simple task template in `tasks.robot`.
  - Uses [Robot Framework](https://robocorp.com/docs/languages-and-frameworks/robot-framework/basics) syntax.
- You can configure your robot `robot.yaml`.
- You can configure dependencies in `conda.yaml`.

## Learning materials

- [Robocorp Developer Training Courses](https://robocorp.com/docs/courses)
- [Documentation links on Robot Framework](https://robocorp.com/docs/languages-and-frameworks/robot-framework)
- [Example bots in Robocorp Portal](https://robocorp.com/portal)

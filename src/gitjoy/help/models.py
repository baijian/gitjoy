# -*- coding: utf-8 -*-

def get_help_info():
    content = "### The Goal of this project\n"
    content = content + "I want to write a codes and documents management system for enterprise,"
    content = content + "you can use it to manage codes and documents"
    content = content + " and you can also exchange opinions with others using issue,"
    content = content + "as a supplement your can use blog to record your daily thought and weekly work-report.\n"

    content = content + "### Login Module\n"
    content = content + "\tThe purpose of login using github oauth2 is that I want to connect GitJoy to GitHub,"
    content = content + "It will provide some cool function later such as transfer your internal open source project to github and so on.\n\n"
    content = content + "***-usage guide***\n\n"
    content = content + "* Login using github account, then it will init a account for you.\n"
    content = content + "* Login using init account with default password ofcourse you must change it later.\n\n"

    content = content + "### Code Management Module\n"
    content = content + "\tIf you know github, I am sure you know how to use GitJoy,just use it right now!\n\n"
    content = content + "***-commands guide***\n\n"
    content = content + "\t* $ git clone git@gitjoy.xxx.xx:baijian/repo\n\n"

    content = content + "### Doc Management Module\n"
    content = content + "\tJust add a docs directory in your repository and write your docs with markdown,"
    content = content + "then in Doc tab you will see your docs.\n"
    content = content + "\tOfcourse, if your repository only have the docs directory, it will be the documents management system.\n\n"
 
    content = content + "### Issue Module\n"
    content = content + "\tJust write issues to exchange opinions.\n\n"

    content = content + "### Blog Module\n"
    content = content + "\tWith this module your can write your learnings and weekly work-report"
    content = content + " with just add markdown file to push to a specific repository.\n"
    content = content + "Your blog file's name must begin with date such as ```2013-07-21-```, "
    content = content + "it's a rule, just obey it.\n\n"
    content = content + "***-usage guide***\n\n"
    content = content + "\t $ git clone git@gitjoy.xxx.xx:<name>/blog\n"
    content = content + "\t $ cd blog\n"
    content = content + "\t $ git add 2013-07-21-work-report.md\n"
    content = content + "\t $ git commit -m \"add work report\"\n"
    content = content + "\t $ git push origin master\n\n"

    content = content + "### Group Module\n"
    content = content + "\t Just group several people together that you can find the people of your group quickly.\n\n"

    return content

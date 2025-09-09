OS="WINDOWS"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="LINUX"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="MACOS"
fi


open-link () {
    echo "Opening link: $1";
    if [[ "MACOS" == "$OS" ]]; then
        if [[ -d "$HOME/code/b9122" ]]; then
            open -a Safari $1;
        else
            open $1
        fi
    fi
}

syllabus () {
    open-link "https://courseworks2.columbia.edu/courses/232050"
    open-link "https://github.com/mm3509/b9122/tree/main/syllabus"
}

office-hours () {
    open-link "https://courseworks2.columbia.edu/courses/232050"
    open-link "https://github.com/mm3509/b9122/tree/main/syllabus#office-hours"
}

discussion () {
    open-link "https://courseworks2.columbia.edu/courses/232050/discussion_topics/1473640"
}

discussions () {
    open-link "https://courseworks2.columbia.edu/courses/232050/discussion_topics"
}

gradescope () {
    open-link "https://www.gradescope.com/courses/1104441"
}

pollev () {
    open-link "https://courseworks2.columbia.edu/courses/232050/external_tools/22456"
    open-link "https://pollev.com/b9122"
}

courseworks () {
    canvas
}

style () {
    which flake8;
    if [ $? -ne 0 ]; then
        pip install flake8
    fi

    which flake8;
    if [ $? -ne 0 ]; then
        echo "Flake8 failed to install, please ask Miguel or a TA for help";
    else
        flake8 $1 --ignore=W504,E128,E127,E303,E251,W291,W391,E302,E305,E241,E261,E261,F841,E124,W292,W293,W503,W504
    fi
}

comments () {
    open-link "https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/"
}

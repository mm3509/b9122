OS="WINDOWS"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="LINUX"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="MACOS"
fi

which python
if [ $? -ne 0 ]; then
    alias python=python3
fi


b9-open-link () {
    echo "Opening link: $1";
    if [[ "MACOS" == "$OS" ]]; then
        if [[ -d "$HOME/code/b9122" ]]; then
            open -a Safari $1;
        else
            open $1
        fi
    else
        start $1
    fi
}

b9-syllabus () {
    b9-open-link "https://courseworks2.columbia.edu/courses/232050"
    b9-open-link "https://github.com/mm3509/b9122/tree/main/syllabus"
}

b9-office-hours () {
    b9-open-link "https://courseworks2.columbia.edu/courses/232050"
    b9-open-link "https://github.com/mm3509/b9122/tree/main/syllabus#office-hours"
}

b9-discussion () {
    b9-open-link "https://courseworks2.columbia.edu/courses/232050/discussion_topics/1473640"
}

b9-discussions () {
    b9-open-link "https://courseworks2.columbia.edu/courses/232050/discussion_topics"
}

b9-gradescope () {
    b9-open-link "https://www.gradescope.com/courses/1104441"
}

b9-pollev () {
    b9-open-link "https://courseworks2.columbia.edu/courses/232050/external_tools/22456"
    b9-open-link "https://pollev.com/b9122"
}

b9-courseworks () {
    canvas
}

b9-style () {
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

b9-guide-comments () {
    b9-open-link "https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/"
}

b9-guide-speed () {
    b9-open-link "https://github.com/mm3509/b9122/blob/main/1-guides/speed.md"
}

b9-guide-style () {
    b9-open-link "https://google.github.io/styleguide/pyguide.html"
    b9-open-link "https://github.com/mm3509/b9122/blob/main/1-guides/style.md"
}

b9-guide-dry () {
    b9-open-link "https://github.com/mm3509/b9122/blob/main/1-guides/dry.md"
}

b9-doctests-verbose () {
    python -m doctest -v -o=ELLIPSIS $1
}

b9-doctests () {
    python -m doctest -o=ELLIPSIS $1
}

b9-github () {
    open-link "https://github.com/mm3509/b9122"
}

b9-canvas () {
    open-link "https://courseworks2.columbia.edu/courses/232050"
}

echo "You have loaded Miguel's code for B9122"

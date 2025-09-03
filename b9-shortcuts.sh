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
    open-link "https://courseworks2.columbia.edu/courses/232050/discussion_topics/1465507"
}

discussions () {
    open-link "https://courseworks2.columbia.edu/courses/232050/discussion_topics"
}

gradescope () {
    open-link "https://www.gradescope.com/courses/1104441"
}

pollev () {
    open-link "https://courseworks2.columbia.edu/courses/232050/external_tools/22456"
}

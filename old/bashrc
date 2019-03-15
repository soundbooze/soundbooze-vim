# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

#export PS1="\e[47m\u@\h \w> \e[m "
#export PS1="> "

#export PKG_CONFIG_PATH=/usr/local/lib64/pkgconfig/
#export LD_LIBRARY_PATH=/usr/local/lib64/

#
#export GL=`pkg-config --libs --cflags freeglut gl`
#export GLW=`pkg-config --libs --cflags glew glfw3`
#export GLIB=`pkg-config --libs --cflags glib-2.0`
#export GTK=`pkg-config --libs --cflags gtk+-2.0`
#export ALSA=`pkg-config --libs --cflags alsa`
#export PULSE=`pkg-config --libs --cflags libpulse-simple`
#export BCC=`pkg-config --libs --cflags libbcc`
#

alias wcap='wcap-decode capture.wcap --yuv4mpeg2 > capture.y4m'

alias cflow='/home/oche/tools/cflow-1.5/src/cflow -Tn'
alias cscope='/home/oche/tools/cscope-15.8b/src/cscope'
alias splint='splint -strict-lib'
alias valgrind='valgrind --leak-check=yes -v'
alias radare2='/home/oche/bin/radare2 -d'

alias straceK='strace -k'
alias straceI='strace -i'

alias weston='weston 2> /dev/null'

cflowURL () {
  url=$1
  basename=`echo ${url//+(*\/|.*)}`
  /usr/bin/curl $1 > /tmp/$basename.c 2> /dev/null
  /home/oche/tools/cflow-1.5/src/cflow -Tn /tmp/$basename.c
  /usr/bin/rm /tmp/$basename.c
}

headerView() {
  if [ "$#" -eq 2 ]
    then
      fgrep -r '#include' $2
    else
      fgrep '#include' $1
  fi
}

defineView() {
  if [ "$#" -eq 2 ]
    then
      fgrep -r '#define' $2
    else
      fgrep '#define' $1
  fi
}

export CSCOPE_EDITOR=gvim
alias cscope='/home/oche/tools/cscope-15.8b/src/cscope -d'

initCscope() {
  find . -name "*.c" -o -name "*.h" > cscope.files
  /home/oche/tools/cscope-15.8b/src/cscope -q -R -b -i cscope.files
}


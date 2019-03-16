# soundbooze-vim
Plugins, Configuration and Setting

### Build

```
./configure --enable-gui=gtk2 --enable-cscope --enable-pythoninterp --prefix=/usr --with-features=huge 
```

### Plugin

#### Vundle

```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

#### Taglist

```
wget -O ~/vimtaglist.zip \
 http://vim.sourceforge.net/scripts/download_script.php?src_id=19574 \
 && cd ~/.vim && unzip ~/vimtaglist.zip
```

#### YouCompleteMe

```
cd ~/.vim/bundle
git clone https://github.com/Valloric/YouCompleteMe.git
cd YouCompleteMe
git submodule update --init --recursive
./install.sh --clang-completer
```

#### Note

```
$ cat ~/.vimrc

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'itchyny/lightline.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'Valloric/YouCompleteMe'

let g:ycm_global_ycm_extra_conf="~/.vim/bundle/YouCompleteMe/third_party/ycmd/ycmd/tests/clang/testdata/.ycm_extra_conf.py"

call vundle#end()

filetype plugin indent on

" Enable Tlist toggle with F8
nnoremap <silent> <F8> :TlistToggle<CR>
map <C-o> :NERDTreeToggle<CR>
```

<pre>
# :PluginInstall
# :NERDTree
# F8
</pre>

#### CSCOPE

```
CTAGS
======

ctags -R *

Ctrl-]  -- Jump to the tag underneath the cursor
:ts <tag> <RET> -- Search for a particular tag
:tn -- Go to the next definition for the last tag
:tp -- Go to the previous definition for the last tag
:ts -- List all of the definitions of the last tag
Ctrl-t -- Jump back up in the tag stack

CSCOPE
======

# plugin
# https://sites.google.com/site/vimcctree/
# :CCTreeLoadDB cscope.out
# :CCTreeTraceForward main

export CSCOPE_EDITOR=`which vim`
cd ~/src/
find . -name "*.c" -o -name "*.h" > cscope.files

# reference
cscope -q -R -b -i cscope.files

# start
cscope -d
```

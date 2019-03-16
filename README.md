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

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

#### CTAGS / CSCOPE

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

#### CFLOW

```
" cflow
command! -complete=shellcmd -nargs=+ Shell call s:RunShellCommand(<q-args>)
function! s:RunShellCommand(cmdline)
  let isfirst = 1
  let words = []
  for word in split(a:cmdline)
    if isfirst
      let isfirst = 0  " don't change first word (shell command)
    else
      if word[0] =~ '\v[%#<]'
        let word = expand(word)
      endif
      let word = shellescape(word, 1)
    endif
    call add(words, word)
  endfor
  let expanded_cmdline = join(words) . ' ' . shellescape(expand('%:p'), 1)
  botright vnew
  setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile nowrap filetype=c
  call setline(1, 'You entered:  ' . a:cmdline)
  call setline(2, 'Expanded to:  ' . expanded_cmdline)
  call append(line('$'), substitute(getline(2), '.', '=', 'g'))
  silent execute '$read !'. expanded_cmdline
  1
endfunction

let g:cflow="off"
function! ToggleCflow()
  if g:cflow == "on"
    let g:cflow="off"
    pclose
  else
    let g:cflow="on"
    :Shell cflow -Tn 
  endif
endfunction

nnoremap <F5> :call ToggleCflow()<CR>
```

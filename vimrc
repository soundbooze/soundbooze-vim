syntax on
set number
set ruler
set ai
set ic
set ts=2
set sw=2
set expandtab
set nowrap
set noswapfile
color jellybeans
set guifont=Monospace\ 11
"set autochdir

:set guioptions-=m  "remove menu bar
:set guioptions-=T  "remove toolbar
:set guioptions-=r  "remove right-hand scroll bar
:set guioptions-=L  "remove left-hand scroll bar

"augroup vimrc
"  au BufReadPre * setlocal foldmethod=indent
"  au BufWinEnter * if &fdm == 'indent' | setlocal foldmethod=manual | endif
"augroup END

"function! Tab_Or_Complete()
"  if col('.')>1 && strpart( getline('.'), col('.')-2, 3 ) =~ '^\w'
"    return "\<C-N>"
"  else
"    return "\<Tab>"
"  endif
"endfunction
":inoremap <Tab> <C-R>=Tab_Or_Complete()<CR>
":set dictionary="/usr/share/dict/words"

nnoremap <silent> <F8> :TlistToggle<CR>

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'itchyny/lightline.vim'
Plugin 'scrooloose/nerdtree'
"Plugin 'Valloric/YouCompleteMe'

call vundle#end()

filetype plugin indent on

" Enable Tlist toggle with F8
nnoremap <silent> <F8> :TlistToggle<CR>

map <C-o> :NERDTreeToggle<CR>

setlocal foldmethod=indent

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
    :Shell /home/oche/cflow-1.5/src/cflow -Tn 
  endif
endfunction

nnoremap <F5> :call ToggleCflow()<CR>
nnoremap <F6> :new<CR>:setlocal syntax=c<CR>p
"nnoremap <F6> :echo line('$')<CR>
"nnoremap <F7> :echo expand('%:p')<CR>

map <S-m> :read ~/.vim/skel/main<CR>
map <S-h> :read ~/.vim/skel/header<CR>

iabbr #i #include
iabbr #d #define
iabbr dou double
iabbr flo float
iabbr reg register
iabbr ext extern
iabbr ret return
iabbr str struct
iabbr sta static
iabbr def default
iabbr uns unsigned
iabbr siz sizeof
iabbr cont continue

iabbr for0 for (i = 0; i < ; i++) {<CR><CR>}
iabbr rof0 for (i = ; i > 0; i--) {<CR><CR>}
iabbr while while () {<CR><CR>}
iabbr switch switch () {<CR><CR>}

iabbr ifdef #ifdef CONFIG_UDUK<CR>#else<CR>#endif

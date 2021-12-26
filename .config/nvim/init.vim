" -------------------SETUPS-------------------
" tabs
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent

" num
set nu
set relativenumber

" search
set nohlsearch
set incsearch

" set true color to the terminal
set termguicolors

" set yank to global. More info: https://www.reddit.com/r/neovim/comments/3fricd/easiest_way_to_copy_from_neovim_to_system/?utm_source=share&utm_medium=web2x&context=3
set clipboard+=unnamedplus

" others
set noerrorbells
set scrolloff=8
set nowrap
set encoding=utf-8

" -------------------KEYBIND--------------------
" map leader
let mapleader = " "

" press jj to return to normal mode in insert mode
inoremap jj <ESC>
inoremap <ESC> <NOP>

" press ii to return to normal mode in visual mode
vnoremap ii <ESC>
vnoremap <ESC> <NOP>

" press ii to return to normal mode in command mode
cnoremap ii <ESC>

" press space-f to open NERDTreeFind in normal mode
nnoremap <leader>f :NERDTreeFind <CR>

" press space-i to enable indent line
nnoremap <leader>i :set cursorcolumn <CR>

" press space-ii to disable indent line
nnoremap <leader>ii :set nocursorcolumn <CR>

" remap the hjkl in to jkl;
"noremap ; l
"noremap l k
"noremap k j
"noremap j h

" press space-k or space-l to move lines down and up respectively
nnoremap <leader>k :m .+1<CR>==
nnoremap <leader>l :m .-2<CR>==
vnoremap <leader>k :m '>+1<CR>gv=gv
vnoremap <leader>l :m '<-2<CR>gv=gv

" make key binding for yank and passte global
" Copy to clipboard
vnoremap  <leader>y  "+y
nnoremap  <leader>Y  "+yg_
nnoremap  <leader>y  "+y
nnoremap  <leader>yy  "+yy

" Paste from clipboard
nnoremap <leader>p "+p
nnoremap <leader>P "+P
vnoremap <leader>p "+p
vnoremap <leader>P "+P

" Press f2 to run python3 script more info: https://stackoverflow.com/a/18948530
autocmd FileType python nnoremap <buffer> <F2> :w<CR>:exec '! clear; python3' shellescape(@%, 1)<CR>
autocmd FileType python inoremap <buffer> <F2> <esc>:w<CR>:exec '! clear; python3' shellescape(@%, 1)<CR>

" --------------------PLUGINS------------------
call plug#begin('~/.vim/plugged')

" gruvbox colorscheme
Plug 'gruvbox-community/gruvbox'

" NERDTree file finder
" Plug 'preservim/nerdtree'

" Syntax for TOML file
" Plug 'cespare/vim-toml'

call plug#end()

"-------------------INITIAL PLUGINS-------------------
" gruvbox colorscheme
colorscheme gruvbox

"NERDTree file finder
" Exit Vim if NERDTree is the only window left.
" autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() |
"    \ quit | endif

" Exit NERDTree after open a file.
" let NERDTreeQuitOnOpen = 3


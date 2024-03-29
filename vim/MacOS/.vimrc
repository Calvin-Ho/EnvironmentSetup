" Sets title of file to be in title bar and disable changing console window
" title when exiting vim
set title
set titleold=""

" Always show the status line
set laststatus=2

" Allow yanked text to be placed into global clipboard
set clipboard=unnamedplus

" Always show current cursor position
set ruler

" Set scrolloff to large value to always center window on cursor
" set scrolloff=5000

" Set command window height to 2 lines
set cmdheight=2

" Set to auto read when a file is changed externally
set autoread

" Show partial commands in the last line of the screen
set showcmd

" Find next match as search is typed
set incsearch

" Set tab to insert 3 spaces upon usage and use smart tabs
set tabstop=3 shiftwidth=3 expandtab
set smarttab

" Turn off word wrap on longer lines
set wrap
set linebreak
set textwidth=0
set wrapmargin=0

" Setting listchars
set showbreak=↪\
set listchars=tab:→\
set listchars+=eol:↲
set listchars+=nbsp:␣
set listchars+=space:•
set listchars+=extends:⟩
set listchars+=precedes:⟨

" Add extra margin to the left
set foldcolumn=1

" No annoying sound on errors
set noerrorbells
set novisualbell

" Allow low delay escaping
set timeoutlen=100

" Enable command line tab completion
" On first tab press:
"     a list of completions will be shown and the command will
"     be completed to the longest common command.
" On second tab press:
"     the wildmenu will show up with all the completions
"     that were listed before.
set wildmenu
set wildmode=list:longest,full

" Highlight characters on a line that exceed 80 chars
" cterm 225 is a light salmon color
highlight ColorColumn ctermbg=225
call matchadd('ColorColumn', '\%81v', 80)

" Show matching brackets when text indicator is over them
set showmatch

" Ignore case when searching, but also use smartcase
set ignorecase
set smartcase

" Attempt to determine the type of a file based on its name and possibly its
" contents.
filetype indent plugin on

" Always highlight search results
set hlsearch

" Remaps <Esc> in normal mode to disable highlighting after search
nnoremap <Esc><Esc> :noh<Return>

" Return to last edit position when opening files
autocmd BufReadPost *
     \ if line("'\"") > 0 && line("'\"") <= line("$") |
     \   exe "normal! g`\"" |
     \ endif

" Turn on line numbers
set number

" Set Vim to use 256 colors
set t_Co=256

" Enable syntax highlighting
syntax on

" Use dark background
set background=dark

" Set color scheme
colorscheme hybrid

" Commenting macro (// in front of line bound to Ctrl + /)
map <C-_> ^i//<ESC>

" Some vim-airline customizations:
"
" Show buffers in the tabline and enable buffer numbers
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_nr_show = 1

" Package Manager [Pathogen]
execute pathogen#infect()

" Vim color file
" Maintainer: Eddie Kovsky
" Version: 1.01
" License: GPLv2

if has("gui_running")
    set background=dark
endif

highlight clear

if exists("syntax_on")
	syntax reset
endif

let colors_name = "blue_in_green"

if ($TERM =~ '256' || &t_Co >= 256) || has("gui_running")
	" Core syntax groups
	hi Normal         ctermbg=0   ctermfg=15   guibg=#263238 guifg=#ffffff
	hi LineNr         ctermbg=0   ctermfg=109  guibg=#263238 guifg=#a7adba
	hi FoldColumn     ctermbg=0   ctermfg=188  guibg=#263238 guifg=#b0bec5
	hi! link signColumn	FoldColumn
	hi! link Folded		FoldColumn
	hi MatchParen     ctermbg=45  ctermfg=0    guibg=#56c3f4 guifg=#ffffff

	" Common syntax groups for programming languages
	" See :help group-name
	"
	" Constant - green
	hi Constant       ctermbg=NONE ctermfg=10  guibg=NONE guifg=#8bc34a
	hi String         ctermbg=NONE ctermfg=10  guibg=NONE guifg=#9ccc65
	hi! link Character              Constant
	hi! link Number                 Constant
	hi! link Boolean                Constant
	hi! link Float                  Constant

	" Variables (identifiers in Vim) are blue; function names are orange.
	" Some Vim syntax files, including c.vim, do not define these groups.
	hi Function     ctermbg=NONE ctermfg=215  guibg=NONE guifg=#ffcc80
	hi Identifier   ctermbg=NONE ctermfg=159  guibg=NONE guifg=#84ffff cterm=NONE gui=NONE

	" Statement - yellow
	hi Statement      ctermbg=NONE ctermfg=228  guibg=NONE guifg=#fff59d gui=NONE
	hi! link Conditional            Statement
	hi! link Repeat                 Statement
	hi! link Label                  Statement
	hi! link Operator               Statement
	hi! link Keyword                Statement
	hi! link Exception              Statement

	" Preprocessor - gold
	hi PreProc        ctermbg=NONE ctermfg=220  guibg=NONE guifg=#ffd700
	hi! link Include                PreProc
	hi! link Define                 PreProc
	hi! link Macro                  PreProc
	hi! link PreCondit              PreProc

	" Type: int, long, char, etc. - aqua
	hi Type           ctermbg=NONE ctermfg=159  guibg=NONE guifg=#84ffff gui=NONE
	hi! link StorageClass           Statement
	hi! link Structure              Statement
	hi! link Typedef                Type

	" Special symbols - orange
	hi Special        ctermbg=NONE ctermfg=208  guibg=NONE guifg=#ff9800
	hi! link Delimiter              Special

	" Blank, hidden, unprintable characters that don't exist inside the text
	hi SpecialKey     ctermbg=NONE ctermfg=240  guibg=NONE guifg=#585858
	hi! link NonText  SpecialKey
	hi Ignore         ctermbg=NONE ctermfg=NONE guibg=NONE guifg=NONE
	hi Conceal        ctermbg=NONE ctermfg=15   guibg=NONE guifg=#ffffff

	" Comment and Todo: keywords TODO FIXME and XXX
	hi Comment        ctermbg=NONE ctermfg=188  guibg=NONE guifg=#b0bec5
	hi Todo           ctermbg=NONE ctermfg=15   guibg=NONE guifg=#ffffff

	"Underlined	text that stands out, HTML links
	hi Underlined     ctermbg=NONE ctermfg=66   guibg=NONE guifg=#5f8787 cterm=underline gui=underline

	" Error: any erroneous construct
	hi Error          ctermbg=NONE ctermfg=162  guibg=NONE guifg=#f36c60 cterm=reverse gui=reverse

	" Cursor highlighting
	hi Cursor         ctermbg=208  ctermfg=0	guibg=#ff9800 guifg=#000000
	hi CursorColumn   ctermbg=237  ctermfg=NONE guibg=#3a3a3a guifg=NONE
	hi CursorLine     ctermbg=237  ctermfg=NONE guibg=#000000 guifg=NONE cterm=NONE
	hi! link CursorLineNr	String

	" Diff mode
	hi diffAdd        ctermbg=64   ctermfg=231  guibg=#437019 guifg=#8bc34a
	hi diffChange     ctermbg=24   ctermfg=NONE guibg=#2b5b77 guifg=#b39ddb
	hi diffDelete     ctermbg=52   ctermfg=162  guibg=#700009 guifg=#f36c60
	hi DiffText       ctermbg=237  ctermfg=38   guibg=#000000 guifg=#8fbfdc cterm=reverse gui=reverse

	" Patch files
	hi! link diffAdded	Constant
	hi diffChanged    ctermbg=NONE ctermfg=159  guibg=NONE    guifg=#ff5722
	hi diffRemoved    ctermbg=NONE ctermfg=9    guibg=NONE    guifg=#f36c60

	hi IncSearch      ctermbg=131  ctermfg=10   guibg=NONE	  guifg=#8bc34a
	hi Search		  ctermbg=10   ctermfg=15   guibg=#8bc34a guifg=#ffffff

	hi Pmenu          ctermbg=237  ctermfg=15   guibg=#3a3a3a guifg=#ffffff
	hi PmenuSbar      ctermbg=188  ctermfg=NONE guibg=#b0bec5 guifg=NONE
	hi PmenuSel       ctermbg=159  ctermfg=240  guibg=#84ffff guifg=#555555
	hi PmenuThumb     ctermbg=159  ctermfg=159  guibg=#84ffff guifg=#84ffff

	hi StatusLine     ctermbg=237  ctermfg=15   guibg=#3a3a3a guifg=#ffffff cterm=NONE gui=NONE
	hi StatusLineNC   ctermbg=237  ctermfg=15   guibg=#3a3a3a guifg=#ffffff cterm=NONE gui=italic

	" TabLine - rarely used
	hi! link TabLine	Pmenu
	hi TabLineFill    ctermbg=237  ctermfg=237  guibg=#3a3a3a guifg=#3a3a3a
	hi TabLineSel     ctermbg=15   ctermfg=240  guibg=#ffffff guifg=#555555

	hi Visual         ctermbg=240  ctermfg=NONE guibg=#555555 guifg=NONE
	hi VisualNOS      ctermbg=NONE ctermfg=NONE guibg=NONE    guifg=NONE    cterm=underline gui=underline

	" Write good
	hi SpellBad   guisp=#bc6c4c guifg=NONE ctermfg=202  ctermbg=237 cterm=NONE gui=undercurl
	hi SpellCap   guisp=#6c6c9c guifg=NONE ctermfg=141  ctermbg=237 cterm=undercurl gui=undercurl
	hi SpellRare  guisp=#bc6c9c guifg=NONE ctermfg=202  ctermbg=237 cterm=NONE gui=undercurl
	hi SpellLocal guisp=#7cac7c guifg=NONE ctermfg=108  ctermbg=237 cterm=undercurl gui=undercurl

	" Menus, etc ...
	hi! link Directory	Identifier
	hi! link MoreMsg	Identifier
	hi ErrorMsg         ctermbg=NONE ctermfg=162   guibg=NONE    guifg=#f36c60
	hi ModeMsg          ctermbg=0    ctermfg=228   guibg=#263238 guifg=#fff59d
	hi Question         ctermbg=NONE ctermfg=117   guibg=NONE    guifg=#4dd0e1
	hi Title            ctermbg=NONE ctermfg=141   guibg=NONE    guifg=#b39ddb
	hi! link VertSplit	TabLineFill
	hi! link WarningMsg	Special
	hi helpLeadBlank    ctermbg=NONE ctermfg=NONE  guibg=NONE    guifg=NONE
	hi! link helpNormal	helpLeadBlank
endif

hi! link htmlEndTag               htmlTagName
hi! link htmlLink                 Function
hi! link htmlSpecialTagName       htmlTagName
hi! link htmlTag                  htmlTagName
hi! link htmlBold                 Normal
hi! link htmlItalic               Normal
hi! link xmlTag                   Statement
hi! link xmlTagName               Statement
hi! link xmlEndTag                Statement

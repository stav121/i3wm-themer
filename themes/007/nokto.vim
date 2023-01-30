" Name: nokto
" Description: black, spacey colorscheme
" Author: Nova Senco <novasenco at protonmail dot ch>
" Last Change: 10 August 2021
" URL: https://github.com/novasenco/nokto
" Type: dark

highlight clear
if exists('syntax_on')
  syntax reset
endif
let colors_name = 'nokto'
if &background isnot 'dark'
  set background=dark
endif

if has('gui_running') || has('termguicolors') && &termguicolors
    let g:terminal_ansi_colors = ['#303030', '#d7005f', '#afd7af', '#af8787', '#87afd7', '#af87af', '#87afaf', '#d0d0d0', '#808080', '#d787af', '#87af5f', '#d7af87', '#5f8787', '#af87d7', '#5faf87', '#e4e4e4']
elseif has('nvim') && !get(g:, 'nokto_no_nvim_term')
  let [g:terminal_color_0,g:terminal_color_1,g:terminal_color_2,g:terminal_color_3,g:terminal_color_4,g:terminal_color_5,g:terminal_color_6,g:terminal_color_7,g:terminal_color_8,g:terminal_color_9,g:terminal_color_10,g:terminal_color_11,g:terminal_color_12,g:terminal_color_13,g:terminal_color_14,g:terminal_color_15] = ['#303030','#d7005f','#afd7af','#af8787','#87afd7','#af87af','#87afaf','#d0d0d0','#808080','#d787af','#87af5f','#d7af87','#5f8787','#af87d7','#5faf87','#e4e4e4']
endif

highlight! link Function Identifier
highlight! link PreProc Identifier
highlight! link Special Identifier
highlight! link Type Identifier
highlight! link HtmlBold Bold
highlight! link HtmlItalic Italic
highlight! link HtmlUnderline Underlined
highlight! link Terminal Normal
highlight! link StatusLineTerm StatusLine
highlight! link StatusLineTermNC StatusLineNC
highlight! link Folded NonText
highlight! link MoreMsg ModeMsg
highlight! link Question ModeMsg
highlight! link SpellCap SpellBad
highlight! link SpellLocal SpellBad
highlight! link SpellRare SpellBad
highlight! link TSConstant Constant
highlight! link TSConstBuiltin Constant
highlight! link TSNumber Number
highlight! link TSFloat Float
highlight! link TSBoolean Boolean
highlight! link TSCharacter Character
highlight! link TSString String
highlight! link TSStringRegex String
highlight! link TSStringEscape String
highlight! link TSProperty TSField
highlight! link TSParameterReference TSParameter
highlight! link TSFunction Function
highlight! link TSFuncBuiltin TSFunction
highlight! link TSFuncMacro TSFunction
highlight! link TSMethod TSFunction
highlight! link TSConstructor TSFunction
highlight! link TSKeyword Keyword
highlight! link TSConditional Conditional
highlight! link TSRepeat Repeat
highlight! link TSLabel Label
highlight! link TSOperator Operator
highlight! link TSException Exception
highlight! link TSNamespace PreProc
highlight! link TSAnnotation TSNamespace
highlight! link TSInclude TSNamespace
highlight! link TSType Type
highlight! link TSTypeBuiltin Type
highlight! link TSPunctDelimiter Delimiter
highlight! link TSPunctSpecial Delimiter
highlight! link TSComment Comment
highlight! link TSTag Tag
highlight! link TSTagDelimiter Special
highlight! link TSLiteral TSString
highlight! link TSURI TSSymbol
" filetype modifications
if get(g:, 'nokto_ft_mods', 1)
  " c
  highlight! link cStorageClass Statement
  highlight! link cEnum Statement
  highlight! link cTypedef Statement
  highlight! link cMacroName Identifier
  highlight! link cDataStructureKeyword Identifier
  " vim
  highlight! link vimHiAttrib Constant
  " markdown
  highlight! link markdownCodeBlock markdownCode
endif

" automatically downgrade if &t_Co is smaller than 256
if (exists('&t_Co') && !empty(&t_Co) && &t_Co > 1 ? &t_Co : 2) < 256
  highlight Normal cterm=NONE ctermfg=7 ctermbg=NONE gui=NONE guifg=#d0d0d0 guibg=#000000
  highlight Constant cterm=NONE ctermfg=9 ctermbg=NONE gui=NONE guifg=#d787af guibg=NONE
  highlight String cterm=NONE ctermfg=2 ctermbg=NONE gui=NONE guifg=#afd7af guibg=NONE
  highlight Identifier cterm=NONE ctermfg=4 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE
  highlight Statement cterm=NONE ctermfg=5 ctermbg=NONE gui=NONE guifg=#af87af guibg=NONE
  highlight Comment cterm=italic ctermfg=8 ctermbg=NONE gui=italic guifg=#808080 guibg=NONE
  highlight Ignore cterm=NONE ctermfg=8 ctermbg=NONE gui=NONE guifg=#808080 guibg=NONE
  highlight Bold cterm=bold ctermfg=NONE ctermbg=NONE gui=bold guifg=NONE guibg=NONE
  highlight Italic cterm=italic ctermfg=NONE ctermbg=NONE gui=italic guifg=NONE guibg=NONE
  highlight Underlined cterm=underline ctermfg=NONE ctermbg=NONE gui=underline guifg=NONE guibg=NONE
  highlight Tag cterm=underline ctermfg=5 ctermbg=NONE gui=underline guifg=#af87af guibg=NONE
  highlight Error cterm=bold,reverse ctermfg=9 ctermbg=NONE gui=bold,reverse guifg=#d787af guibg=NONE
  highlight Todo cterm=bold,reverse ctermfg=6 ctermbg=NONE gui=bold,reverse guifg=#87afaf guibg=NONE
  highlight NormalFloat cterm=NONE ctermfg=NONE ctermbg=0 gui=NONE guifg=NONE guibg=#1c1c1c
  highlight StatusLine cterm=NONE ctermfg=7 ctermbg=0 gui=NONE guifg=#d0d0d0 guibg=#444444
  highlight StatusLineNC cterm=NONE ctermfg=3 ctermbg=0 gui=NONE guifg=#af8787 guibg=#303030
  highlight TabLine cterm=NONE ctermfg=3 ctermbg=0 gui=NONE guifg=#af8787 guibg=#303030
  highlight TabLineFill cterm=NONE ctermfg=0 ctermbg=0 gui=NONE guifg=#303030 guibg=#303030
  highlight TabLineSel cterm=NONE ctermfg=7 ctermbg=0 gui=NONE guifg=#d0d0d0 guibg=#262626
  highlight Pmenu cterm=NONE ctermfg=7 ctermbg=0 gui=NONE guifg=#a8a8a8 guibg=#1c1c1c
  highlight PmenuSel cterm=reverse ctermfg=3 ctermbg=NONE gui=reverse guifg=#af8787 guibg=NONE
  highlight PmenuSbar cterm=reverse ctermfg=0 ctermbg=NONE gui=reverse guifg=#303030 guibg=NONE
  highlight PmenuThumb cterm=reverse ctermfg=6 ctermbg=NONE gui=reverse guifg=#87afaf guibg=NONE
  highlight WildMenu cterm=bold,reverse ctermfg=11 ctermbg=NONE gui=bold,reverse guifg=#d7af87 guibg=NONE
  highlight Title cterm=italic,bold ctermfg=6 ctermbg=NONE gui=italic,bold guifg=#87afaf guibg=NONE
  highlight SpecialKey cterm=NONE ctermfg=8 ctermbg=NONE gui=NONE guifg=#808080 guibg=NONE
  highlight NonText cterm=italic ctermfg=4 ctermbg=0 gui=italic guifg=#87afd7 guibg=#1c1c1c
  highlight EndOfBuffer cterm=NONE ctermfg=4 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE
  highlight Search cterm=bold ctermfg=0 ctermbg=6 gui=bold guifg=#000000 guibg=#87afaf
  highlight IncSearch cterm=bold ctermfg=0 ctermbg=11 gui=bold guifg=#000000 guibg=#d7af87
  highlight QuickFixLine cterm=bold ctermfg=NONE ctermbg=0 gui=bold guifg=NONE guibg=#303030
  highlight Conceal cterm=NONE ctermfg=4 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE
  highlight Cursor cterm=NONE ctermfg=0 ctermbg=7 gui=NONE guifg=#000000 guibg=#d0d0d0
  highlight lCursor cterm=NONE ctermfg=0 ctermbg=7 gui=NONE guifg=#000000 guibg=#d0d0d0
  highlight CursorIM cterm=NONE ctermfg=0 ctermbg=7 gui=NONE guifg=#000000 guibg=#d0d0d0
  highlight Directory cterm=NONE ctermfg=4 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE
  highlight ErrorMsg cterm=bold,reverse ctermfg=9 ctermbg=NONE gui=bold,reverse guifg=#d787af guibg=NONE
  highlight WarningMsg cterm=bold,reverse ctermfg=11 ctermbg=NONE gui=bold,reverse guifg=#d7af87 guibg=NONE
  highlight ModeMsg cterm=bold ctermfg=11 ctermbg=NONE gui=bold guifg=#d7af87 guibg=NONE
  highlight SpellBad cterm=bold,reverse ctermfg=9 ctermbg=NONE gui=bold,reverse guifg=#d787af guibg=NONE
  highlight DiffAdd cterm=bold ctermfg=0 ctermbg=6 gui=bold guifg=#000000 guibg=#87afaf
  highlight DiffDelete cterm=NONE ctermfg=9 ctermbg=9 gui=NONE guifg=#d787af guibg=#d787af
  highlight DiffChange cterm=NONE ctermfg=0 ctermbg=4 gui=NONE guifg=#000000 guibg=#87afd7
  highlight DiffText cterm=bold ctermfg=0 ctermbg=11 gui=bold guifg=#000000 guibg=#d7af87
  highlight DiffAdded cterm=bold ctermfg=6 ctermbg=0 gui=bold guifg=#87afaf guibg=#1c1c1c
  highlight DiffRemoved cterm=bold ctermfg=9 ctermbg=0 gui=bold guifg=#d787af guibg=#1c1c1c
  highlight ColorColumn cterm=NONE ctermfg=NONE ctermbg=0 gui=NONE guifg=NONE guibg=#1c1c1c
  highlight CursorColumn cterm=NONE ctermfg=NONE ctermbg=0 gui=NONE guifg=NONE guibg=#1c1c1c
  highlight CursorLine cterm=NONE ctermfg=NONE ctermbg=0 gui=NONE guifg=NONE guibg=#1c1c1c
  highlight Visual cterm=NONE ctermfg=NONE ctermbg=0 gui=NONE guifg=NONE guibg=#303030
  highlight VisualNOS cterm=NONE ctermfg=NONE ctermbg=0 gui=NONE guifg=NONE guibg=#303030
  highlight VertSplit cterm=NONE ctermfg=8 ctermbg=NONE gui=NONE guifg=#808080 guibg=NONE
  highlight LineNr cterm=NONE ctermfg=3 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
  highlight CursorLineNr cterm=NONE ctermfg=3 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
  highlight LineNrAbove cterm=NONE ctermfg=3 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
  highlight LineNrBelow cterm=NONE ctermfg=3 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
  highlight FoldColumn cterm=NONE ctermfg=3 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
  highlight SignColumn cterm=NONE ctermfg=3 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
  highlight MatchParen cterm=bold ctermfg=0 ctermbg=6 gui=bold guifg=#000000 guibg=#87afaf
  highlight TSConstMacro cterm=bold ctermfg=9 ctermbg=NONE gui=bold guifg=#d787af guibg=NONE
  highlight TSSymbol cterm=bold ctermfg=5 ctermbg=NONE gui=bold guifg=#af87af guibg=NONE
  highlight TSField cterm=NONE ctermfg=7 ctermbg=NONE gui=NONE guifg=#d0d0d0 guibg=NONE
  highlight TSParameter cterm=NONE ctermfg=7 ctermbg=NONE gui=NONE guifg=#d0d0d0 guibg=NONE
  highlight TSVariable cterm=NONE ctermfg=7 ctermbg=NONE gui=NONE guifg=#d0d0d0 guibg=NONE
  highlight TSVariableBuiltin cterm=NONE ctermfg=4 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE
  highlight TSKeywordFunction cterm=NONE ctermfg=2 ctermbg=NONE gui=NONE guifg=#afd7af guibg=NONE
  highlight TSPunctBracket cterm=NONE ctermfg=3 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
  highlight TSText cterm=NONE ctermfg=7 ctermbg=NONE gui=NONE guifg=#d0d0d0 guibg=NONE
  highlight TSEmphasis cterm=italic ctermfg=7 ctermbg=NONE gui=italic guifg=#d0d0d0 guibg=NONE
  highlight TSUnderline cterm=underline ctermfg=7 ctermbg=NONE gui=underline guifg=#d0d0d0 guibg=NONE
  highlight TSStrike cterm=underline ctermfg=8 ctermbg=NONE gui=underline guifg=#808080 guibg=NONE
  highlight TSStrong cterm=bold ctermfg=7 ctermbg=NONE gui=bold guifg=#d0d0d0 guibg=NONE
  highlight TSTitle cterm=NONE ctermfg=3 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
  highlight TSError cterm=NONE ctermfg=1 ctermbg=NONE gui=NONE guifg=#d7005f guibg=NONE
  highlight vimCommentTitle cterm=italic ctermfg=7 ctermbg=NONE gui=italic guifg=#a8a8a8 guibg=NONE
  highlight markdownCode cterm=NONE ctermfg=3 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
  finish
endif

highlight Normal cterm=NONE ctermfg=252 ctermbg=16 gui=NONE guifg=#d0d0d0 guibg=#000000

" |group-name|

highlight Constant cterm=NONE ctermfg=175 ctermbg=NONE gui=NONE guifg=#d787af guibg=NONE
highlight String cterm=NONE ctermfg=151 ctermbg=NONE gui=NONE guifg=#afd7af guibg=NONE
highlight Identifier cterm=NONE ctermfg=110 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE
highlight Statement cterm=NONE ctermfg=139 ctermbg=NONE gui=NONE guifg=#af87af guibg=NONE

highlight Comment cterm=italic ctermfg=244 ctermbg=NONE gui=italic guifg=#808080 guibg=NONE
highlight Ignore cterm=NONE ctermfg=244 ctermbg=NONE gui=NONE guifg=#808080 guibg=NONE

highlight Bold cterm=bold ctermfg=NONE ctermbg=NONE gui=bold guifg=NONE guibg=NONE
highlight Italic cterm=italic ctermfg=NONE ctermbg=NONE gui=italic guifg=NONE guibg=NONE
highlight Underlined cterm=underline ctermfg=NONE ctermbg=NONE gui=underline guifg=NONE guibg=NONE
highlight Tag cterm=underline ctermfg=139 ctermbg=NONE gui=underline guifg=#af87af guibg=NONE

highlight Error cterm=bold,reverse ctermfg=175 ctermbg=NONE gui=bold,reverse guifg=#d787af guibg=NONE
highlight Todo cterm=bold,reverse ctermfg=109 ctermbg=NONE gui=bold,reverse guifg=#87afaf guibg=NONE

" |highlight-groups|

highlight NormalFloat cterm=NONE ctermfg=NONE ctermbg=234 gui=NONE guifg=NONE guibg=#1c1c1c

highlight StatusLine cterm=NONE ctermfg=252 ctermbg=238 gui=NONE guifg=#d0d0d0 guibg=#444444
highlight StatusLineNC cterm=NONE ctermfg=138 ctermbg=236 gui=NONE guifg=#af8787 guibg=#303030

highlight TabLine cterm=NONE ctermfg=138 ctermbg=236 gui=NONE guifg=#af8787 guibg=#303030
highlight TabLineFill cterm=NONE ctermfg=236 ctermbg=236 gui=NONE guifg=#303030 guibg=#303030
highlight TabLineSel cterm=NONE ctermfg=252 ctermbg=235 gui=NONE guifg=#d0d0d0 guibg=#262626

highlight Pmenu cterm=NONE ctermfg=248 ctermbg=234 gui=NONE guifg=#a8a8a8 guibg=#1c1c1c
highlight PmenuSel cterm=reverse ctermfg=138 ctermbg=NONE gui=reverse guifg=#af8787 guibg=NONE
highlight PmenuSbar cterm=reverse ctermfg=236 ctermbg=NONE gui=reverse guifg=#303030 guibg=NONE
highlight PmenuThumb cterm=reverse ctermfg=109 ctermbg=NONE gui=reverse guifg=#87afaf guibg=NONE

highlight WildMenu cterm=bold,reverse ctermfg=180 ctermbg=NONE gui=bold,reverse guifg=#d7af87 guibg=NONE

highlight Title cterm=italic,bold ctermfg=109 ctermbg=NONE gui=italic,bold guifg=#87afaf guibg=NONE
highlight SpecialKey cterm=NONE ctermfg=244 ctermbg=NONE gui=NONE guifg=#808080 guibg=NONE

highlight NonText cterm=italic ctermfg=110 ctermbg=234 gui=italic guifg=#87afd7 guibg=#1c1c1c

highlight EndOfBuffer cterm=NONE ctermfg=110 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE

highlight Search cterm=bold ctermfg=16 ctermbg=109 gui=bold guifg=#000000 guibg=#87afaf
highlight IncSearch cterm=bold ctermfg=16 ctermbg=180 gui=bold guifg=#000000 guibg=#d7af87
highlight QuickFixLine cterm=bold ctermfg=NONE ctermbg=236 gui=bold guifg=NONE guibg=#303030

highlight Conceal cterm=NONE ctermfg=110 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE
highlight Cursor cterm=NONE ctermfg=16 ctermbg=252 gui=NONE guifg=#000000 guibg=#d0d0d0
highlight lCursor cterm=NONE ctermfg=16 ctermbg=252 gui=NONE guifg=#000000 guibg=#d0d0d0
highlight CursorIM cterm=NONE ctermfg=16 ctermbg=252 gui=NONE guifg=#000000 guibg=#d0d0d0

highlight Directory cterm=NONE ctermfg=110 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE

highlight ErrorMsg cterm=bold,reverse ctermfg=175 ctermbg=NONE gui=bold,reverse guifg=#d787af guibg=NONE
highlight WarningMsg cterm=bold,reverse ctermfg=180 ctermbg=NONE gui=bold,reverse guifg=#d7af87 guibg=NONE

highlight ModeMsg cterm=bold ctermfg=180 ctermbg=NONE gui=bold guifg=#d7af87 guibg=NONE

highlight SpellBad cterm=bold,reverse ctermfg=175 ctermbg=NONE gui=bold,reverse guifg=#d787af guibg=NONE

highlight DiffAdd cterm=bold ctermfg=16 ctermbg=109 gui=bold guifg=#000000 guibg=#87afaf
highlight DiffDelete cterm=NONE ctermfg=175 ctermbg=175 gui=NONE guifg=#d787af guibg=#d787af
highlight DiffChange cterm=NONE ctermfg=16 ctermbg=110 gui=NONE guifg=#000000 guibg=#87afd7
highlight DiffText cterm=bold ctermfg=16 ctermbg=180 gui=bold guifg=#000000 guibg=#d7af87

highlight DiffAdded cterm=bold ctermfg=109 ctermbg=234 gui=bold guifg=#87afaf guibg=#1c1c1c
highlight DiffRemoved cterm=bold ctermfg=175 ctermbg=234 gui=bold guifg=#d787af guibg=#1c1c1c

highlight ColorColumn cterm=NONE ctermfg=NONE ctermbg=234 gui=NONE guifg=NONE guibg=#1c1c1c
highlight CursorColumn cterm=NONE ctermfg=NONE ctermbg=234 gui=NONE guifg=NONE guibg=#1c1c1c
highlight CursorLine cterm=NONE ctermfg=NONE ctermbg=234 gui=NONE guifg=NONE guibg=#1c1c1c

highlight Visual cterm=NONE ctermfg=NONE ctermbg=236 gui=NONE guifg=NONE guibg=#303030
highlight VisualNOS cterm=NONE ctermfg=NONE ctermbg=236 gui=NONE guifg=NONE guibg=#303030

highlight VertSplit cterm=NONE ctermfg=244 ctermbg=NONE gui=NONE guifg=#808080 guibg=NONE

highlight LineNr cterm=NONE ctermfg=138 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
highlight CursorLineNr cterm=NONE ctermfg=138 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
highlight LineNrAbove cterm=NONE ctermfg=138 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
highlight LineNrBelow cterm=NONE ctermfg=138 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
highlight FoldColumn cterm=NONE ctermfg=138 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE
highlight SignColumn cterm=NONE ctermfg=138 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE

highlight MatchParen cterm=bold ctermfg=16 ctermbg=109 gui=bold guifg=#000000 guibg=#87afaf

highlight TSConstMacro cterm=bold ctermfg=175 ctermbg=NONE gui=bold guifg=#d787af guibg=NONE
highlight TSSymbol cterm=bold ctermfg=139 ctermbg=NONE gui=bold guifg=#af87af guibg=NONE

highlight TSField cterm=NONE ctermfg=252 ctermbg=NONE gui=NONE guifg=#d0d0d0 guibg=NONE
highlight TSParameter cterm=NONE ctermfg=252 ctermbg=NONE gui=NONE guifg=#d0d0d0 guibg=NONE
highlight TSVariable cterm=NONE ctermfg=252 ctermbg=NONE gui=NONE guifg=#d0d0d0 guibg=NONE
highlight TSVariableBuiltin cterm=NONE ctermfg=110 ctermbg=NONE gui=NONE guifg=#87afd7 guibg=NONE

highlight TSKeywordFunction cterm=NONE ctermfg=151 ctermbg=NONE gui=NONE guifg=#afd7af guibg=NONE

highlight TSPunctBracket cterm=NONE ctermfg=138 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE

highlight TSText cterm=NONE ctermfg=252 ctermbg=NONE gui=NONE guifg=#d0d0d0 guibg=NONE
highlight TSEmphasis cterm=italic ctermfg=252 ctermbg=NONE gui=italic guifg=#d0d0d0 guibg=NONE
highlight TSUnderline cterm=underline ctermfg=252 ctermbg=NONE gui=underline guifg=#d0d0d0 guibg=NONE
highlight TSStrike cterm=underline ctermfg=244 ctermbg=NONE gui=underline guifg=#808080 guibg=NONE
highlight TSStrong cterm=bold ctermfg=252 ctermbg=NONE gui=bold guifg=#d0d0d0 guibg=NONE
highlight TSTitle cterm=NONE ctermfg=138 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE

highlight TSError cterm=NONE ctermfg=161 ctermbg=NONE gui=NONE guifg=#d7005f guibg=NONE

highlight vimCommentTitle cterm=italic ctermfg=248 ctermbg=NONE gui=italic guifg=#a8a8a8 guibg=NONE
highlight markdownCode cterm=NONE ctermfg=138 ctermbg=NONE gui=NONE guifg=#af8787 guibg=NONE


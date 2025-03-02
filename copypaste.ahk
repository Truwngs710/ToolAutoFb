F1::
Send, {RButton}  ; Nhấn chuột phải
Sleep, 200       ; Dừng 0.1 giây
Send, {Down 7}   ; Xuống 6 lần
Sleep, 280
Send, {Enter}    ; Nhấn Enter
return

F2::
Send, {LButton}  ; Nhấn chuột trái
Sleep, 150
Send, ^v         ; Nhấn Ctrl + V (dán)
return
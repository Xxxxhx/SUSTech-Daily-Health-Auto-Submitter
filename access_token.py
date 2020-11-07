import win32api
import win32con
import win32gui
import win32clipboard
import time

def find_access_token():
    contract_pos = (30, 140)
    sustech_pos = (165, 385)
    report_pos = (890, 220)
    enter_pos = (1135, 405)
    browser_pos = (640, 730)
    link_pos = (175, 55)
    
    handle = win32gui.FindWindow('WeChatMainWndForPC', '微信')
    win32api.keybd_event(13, 0, 0, 0)
    win32gui.SetForegroundWindow(handle)
    # resize the wechat window
    pos = win32gui.GetWindowRect(handle)
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, pos[0], pos[1], 1000, 750, win32con.SWP_SHOWWINDOW)
    # click contracts button
    win32api.SetCursorPos((pos[0] + contract_pos[0], pos[1] + contract_pos[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.05)
    # click SUSTech
    win32api.SetCursorPos((pos[0] + sustech_pos[0], pos[1] + sustech_pos[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.05)
    # enter dalay health report
    win32api.SetCursorPos((pos[0] + report_pos[0], pos[1] + report_pos[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.05)
    # enter official accounts
    win32api.SetCursorPos((pos[0] + enter_pos[0], pos[1] + enter_pos[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.05)
    # enter internal browser
    win32api.SetCursorPos((pos[0] + browser_pos[0], pos[1] + browser_pos[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.05)

    web_handle = win32gui.FindWindow('CefWebViewWnd', '微信')
    web_pos = win32gui.GetWindowRect(web_handle)

    # copy the link
    win32api.SetCursorPos((web_pos[0] + link_pos[0], web_pos[1] + link_pos[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.15)
    # close the internal browser
    win32api.SendMessage(web_handle, win32con.WM_CLOSE, 0, 0)
    time.sleep(0.05)
    # minimize the window
    win32gui.ShowWindow(handle, win32con.SW_MINIMIZE)

    win32clipboard.OpenClipboard()
    link = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    access_token = link[link.rfind('=') + 1:]

    return access_token


if __name__ == "__main__":
    print(find_access_token())
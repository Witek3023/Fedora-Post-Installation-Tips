# How to Make KDE Faster

## Baloo Configuration

1. **Disable Baloo:**

   ```shell
   balooctl6 disable
   ```

2. **Optimize Baloo:** Edit `~/.config/baloofilerc` to exclude directories.

## Disabling Akonadi

1. **Stop server:**

   ```bash
   akonadictl stop
   ```

2. **Edit config:** In `~/.config/akonadi/akonadiserverrc`, set `StartServer=false`.

## Desktop Effects

* Navigate to **System Settings** > **Apps & Windows** > **Window Manager** > **Desktop Effects**.
* Disable **Blur**, **Fade**, and **Sliding Popups**.

## Background Services

* Navigate to **System Settings** > **Background Services**.
* Disable unused services like **Vaults**, **SMB Watcher**, or **Write Daemon**.

## Plasma Search

* Navigate to **System Settings** > **Workspace** > **Search** > **Plasma Search**.
* Uncheck categories you do not use.

## Animation Speed

* Navigate to **System Settings** > **Workspace** > **General Behavior**.
* Set **Animation speed** to **Instant**.

## User Feedback

* Navigate to **System Settings** > **Security & Privacy** > **User Feedback**.
* Set level to **None**.

# Fedora Post-Install Optimization Guide (Sway/Minimal)

Quick Guide to disable unnecessary background services, free up RAM, and reduce CPU usage.

---

## 1. System Services (Requires `sudo`)

### Disable Crash Reporting (ABRT)

```bash
sudo systemctl disable --now abrtd.service abrt-oops.service abrt-xorg.service abrt-journal-core.service
```

### Disable Cellular Modems & Smart Cards

```bash
sudo systemctl disable --now ModemManager.service pcscd.service
```

### Fix CPU/Battery Conflict (Disable Tuned to use TLP)

```bash
sudo systemctl disable --now tuned.service
```

---

## 2. Disable PackageKit (Automatic Updates)

Prevents background DNF locks and reduces RAM usage. Update manually using.

```bash
sudo killall packagekitd
sudo systemctl stop packagekit
sudo systemctl mask packagekit
```

---

## 3. User Services (Do NOT use `sudo`)

### Disable Bluetooth File Transfer (OBEX)

*Keeps headphone/mouse connectivity active, but stops file sharing.*

```bash
systemctl --user disable --now obex.service
```

### Disable Accessibility APIs (Screen Readers)

```bash
systemctl --user disable --now at-spi-dbus-bus.service
```

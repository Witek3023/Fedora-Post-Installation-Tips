Domyślnie Fedora, zgodnie z polityką swojego systemu operacyjnego, korzysta z oprogramowania otwartoźródłowego (open-source). Aby móc instalować oprogramowanie / sterowniki o zamkniętym dostępie do kodu źródłowego dodaj repozytorium RPM Fusion.

Wprowadź poniższy kod do terminala, aby zainstalować repozytorium RPM Fusion:

sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm


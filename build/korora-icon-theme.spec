%define git d094db7

Name:           korora-icon-theme
Version:        0.2
Release:        1%{?dist}
Summary:        Icons for the Korora Project
License:        GPLv3
URL:            https://kororaproject.org/
Source0:        https://github.com/numixproject/numix-icon-theme-circle/tarball/%{git}
Patch0:         0001-updated-icon-theme-name-change-and-updated-inherits.patch
Patch1:         0002-added-initial-kororification-of-gitk-icon.patch
Patch2:         0003-added-new-qt4-logo-alias-for-qt4logo-icon.patch
Patch3:         0004-added-kororified-lash-icon.patch
Patch4:         0005-added-kororified-welcome-icon.patch
Patch5:         0006-added-kororified-pharlap-icon.patch
Patch6:         0007-added-new-ardour-alias-for-ardour2.patch

BuildArch:      noarch

%description
This is an icon theme based on the Numix project that has been adapated to the
Korora Project styling.

%prep
%setup -q -n numixproject-numix-icon-theme-circle-%{git}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}/icons/korora
cp -apR Numix-Circle/* %{buildroot}%{_datadir}/icons/korora
chmod 644 %{buildroot}%{_datadir}/icons/korora/index.theme

%post
touch --no-create %{_datadir}/icons/korora &>/dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/korora &>/dev/null
  gtk-update-icon-cache -q %{_datadir}/icons/korora &>/dev/null ||:
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/korora &>/dev/null ||:

%files
%doc license
%{_datadir}/icons/korora/

%changelog
* Sat Nov 15 2014 Ian Firns <firnsy@kororaproject.org> - 0.2-1
- Updated to latest upstream.

* Sat Oct 04 2014 Ian Firns <firnsy@kororaproject.org> - 0.1-1
- Intial rpm build

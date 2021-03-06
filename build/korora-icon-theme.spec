#%define git ac4b41d
%define git 84cf0de

Name:           korora-icon-theme
Version:        0.5
Release:        1%{?dist}
Summary:        Icons for the Korora Project
License:        GPLv3
URL:            https://kororaproject.org/
Source0:        https://github.com/numixproject/numix-icon-theme-circle/tarball/%{git}
Source1:        anaconda.svg
Patch0:         0001-updated-icon-theme-name-change-and-updated-inherits.patch
Patch1:         0002-added-initial-kororification-of-gitk-icon.patch
Patch2:         0003-added-new-qt4-logo-alias-for-qt4logo-icon.patch
Patch3:         0004-added-kororified-lash-icon.patch
Patch4:         0005-added-kororified-welcome-icon.patch
Patch5:         0006-added-kororified-pharlap-icon.patch
Patch6:         0007-added-new-ardour-alias-for-ardour2.patch
BuildArch:      noarch
Requires:       korora-icon-theme-base

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
install %{SOURCE1} %{buildroot}%{_datadir}/icons/korora/scalable/apps/
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
%{_datadir}/icons/korora/*

%changelog
* Fri Jan  8 2016 Ian Firns <firnsy@kororaproject.org> - 0.5-1
- Updated to latest upstream.

* Thu Jun  4 2015 Ian Firns <firnsy@kororaproject.org> - 0.4-1
- Updated to latest upstream.

* Thu Feb 19 2015 Chris Smart <csmart@kororaproject.org> - 0.3-1
- Updated to latest upstream.

* Wed Dec 31 2014 Chris Smart <csmart@kororaproject.org> - 0.2-2
- Updated to latest upstream, added anaconda icon

* Sat Nov 15 2014 Ian Firns <firnsy@kororaproject.org> - 0.2-1
- Updated to latest upstream.

* Sat Oct 04 2014 Ian Firns <firnsy@kororaproject.org> - 0.1-1
- Intial rpm build

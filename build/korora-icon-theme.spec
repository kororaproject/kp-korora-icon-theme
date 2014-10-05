Name:           korora-icon-theme
Version:        0.1
Release:        1%{?dist}
Summary:        Icons for the Korora Project
License:        GPLv3
URL:            https://kororaproject.org/
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is an icon theme based on the Numix project that has been adapated to the
Korora Project styling.

%prep
%setup -q

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
* Sat Oct 04 2014 Ian Firns <firnsy@kororaproject.org> - 0.1-1
- Intial rpm build

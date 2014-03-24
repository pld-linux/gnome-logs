Summary:	A log viewer for the systemd journal
Name:		gnome-logs
Version:	3.12.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-logs/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	24ea9833011eef71b666b38e77f51f9d
URL:		https://wiki.gnome.org/Apps/Logs
BuildRequires:	appdata-tools
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-common
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	gsettings-desktop-schemas
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Logs is a viewer for the systemd journal.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-logs
%{_datadir}/appdata/gnome-logs.appdata.xml
%{_desktopdir}/gnome-logs.desktop
%{_mandir}/man1/gnome-logs.1*
%{_iconsdir}/hicolor/*/*/*.png

Summary:	A log viewer for the systemd journal
Summary(pl.UTF-8):	Przeglądarka logów z kroniki systemd
Name:		gnome-logs
Version:	3.24.2
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-logs/3.24/%{name}-%{version}.tar.xz
# Source0-md5:	6dc913951edd0ec8a278501608ca2d4b
URL:		https://wiki.gnome.org/Apps/Logs
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-common
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.44.0
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.20.0
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Logs is a viewer for the systemd journal.

%description -l pl.UTF-8
GNOME Logs to przeglądarka kroniki systemd.

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
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-logs
%{_datadir}/appdata/org.gnome.Logs.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Logs.service
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.gschema.xml
%{_desktopdir}/org.gnome.Logs.desktop
%{_mandir}/man1/gnome-logs.1*
%{_iconsdir}/hicolor/*x*/apps/gnome-logs.png
%{_iconsdir}/hicolor/symbolic/apps/gnome-logs-symbolic.svg

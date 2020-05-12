Summary:	A log viewer for the systemd journal
Summary(pl.UTF-8):	Przeglądarka logów z kroniki systemd
Name:		gnome-logs
Version:	3.36.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-logs/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	fc25928b4ffad25e27b3755751b4b323
URL:		https://wiki.gnome.org/Apps/Logs
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libxslt-progs
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.44.0
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.22.0
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Logs is a viewer for the systemd journal.

%description -l pl.UTF-8
GNOME Logs to przeglądarka kroniki systemd.

%prep
%setup -q

%build
%meson build \
	-Dman=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-logs
%{_datadir}/dbus-1/services/org.gnome.Logs.service
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.Logs.gschema.xml
%{_datadir}/gnome-logs
%{_datadir}/metainfo/org.gnome.Logs.appdata.xml
%{_desktopdir}/org.gnome.Logs.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Logs.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Logs-symbolic.svg
%{_mandir}/man1/gnome-logs.1*

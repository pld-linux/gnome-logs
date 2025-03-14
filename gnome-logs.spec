# TODO: switch to gtk4-update-icon-cache
Summary:	A log viewer for the systemd journal
Summary(pl.UTF-8):	Przeglądarka logów z kroniki systemd
Name:		gnome-logs
Version:	45.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-logs/45/%{name}-%{version}.tar.xz
# Source0-md5:	5b9396cf24528ae72eb4c48934f60df2
URL:		https://apps.gnome.org/Logs/
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk4-devel >= 4.10.0
BuildRequires:	libadwaita-devel >= 1.4
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.44.0
Requires:	gsettings-desktop-schemas
Requires:	gtk4 >= 4.10.0
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Logs is a viewer for the systemd journal.

%description -l pl.UTF-8
GNOME Logs to przeglądarka kroniki systemd.

%prep
%setup -q

%build
%meson \
	-Dman=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
%{_datadir}/metainfo/org.gnome.Logs.appdata.xml
%{_desktopdir}/org.gnome.Logs.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Logs.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Logs-symbolic.svg
%{_mandir}/man1/gnome-logs.1*

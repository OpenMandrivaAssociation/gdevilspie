%define name gdevilspie
%define version 0.31
%define release %mkrel 5

Summary: GTK GUI for devilspie
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPLv3+
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: desktop-file-utils
Requires: devilspie
Requires: pygtk2.0-libglade
Requires: gnome-python-desktop
Url: http://code.google.com/p/gdevilspie/

%description
A user friendly interface to the devilspie window matching daemon, to
create rules easily.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

desktop-file-install --vendor="" \
  --remove-category="Utility" \
  --add-category="GTK" \
  --add-category="Settings" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO Changelog
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/%name
%_datadir/pixmaps/%name.png
%py_puresitedir/g*


%changelog
* Fri Nov 04 2011 Götz Waschk <waschk@mandriva.org> 0.31-5mdv2012.0
+ Revision: 717578
- rebuild

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 0.31-4mdv2011.0
+ Revision: 592835
- rebuild for new python 2.7

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.31-3mdv2011.0
+ Revision: 437666
- rebuild

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.31-2mdv2009.1
+ Revision: 320640
- rebuild for new python

* Tue Jun 17 2008 Götz Waschk <waschk@mandriva.org> 0.31-1mdv2009.0
+ Revision: 222013
- new version

* Tue Apr 01 2008 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2008.1
+ Revision: 191344
- import gdevilspie



Summary:	GTK GUI for devilspie
Name:		gdevilspie
Version:	0.5
Release:	1
Epoch:		1
License:	GPLv3+
Group:		Graphical desktop/GNOME
Url:		http://code.google.com/p/gdevilspie/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(python)
Requires:	devilspie
Requires:	pygtk2.0-libglade
Requires:	gnome-python-desktop
BuildArch:	noarch

%description
A user friendly interface to the devilspie window matching daemon, to
create rules easily.

%files
%doc README TODO Changelog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{py_puresitedir}/g*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}



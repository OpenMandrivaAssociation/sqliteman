Summary:	Lightweigth but powerfull Sqlite3 manager
Name:		sqliteman
Version:	1.2.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Databases
URL:		http://sqliteman.sourceforge.net/
Source:		http://downloads.sourceforge.net/sqliteman/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel >= 4.3.0
%if %mdkversion < 200900
BuildRequires:	qt4-database-plugin-sqlite-lib
%else
BuildRequires:	qt4-database-plugin-sqlite
%endif
BuildRequires:	cmake
BuildRequires:	qscintilla-qt4-devel
%if %mdkversion < 200900
Requires:	qt4-database-plugin-sqlite-lib
%else
Requires:	qt4-database-plugin-sqlite
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The best developer's and/or admin's GUI tool for Sqlite3
in the world. No joking here (or just a bit only) - it
contains the most complette feature set of all tools available.

%prep
%setup -q

%build
%cmake_qt4
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std -C build

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_datadir}/%{name}/doc/*
%{_bindir}/sqliteman
%{_datadir}/applications/sqliteman.desktop
%{_datadir}/%{name}/icons/*.png
%{_iconsdir}/hicolor/sqliteman.png
%lang(bg) %{_datadir}/%{name}/sqliteman_bg.qm
%lang(cs) %{_datadir}/%{name}/sqliteman_cs.qm
%lang(de) %{_datadir}/%{name}/sqliteman_de.qm
%lang(en) %{_datadir}/%{name}/sqliteman_en.qm
%lang(fr) %{_datadir}/%{name}/sqliteman_fr.qm
%lang(it) %{_datadir}/%{name}/sqliteman_it.qm
%lang(pl) %{_datadir}/%{name}/sqliteman_pl.qm
%lang(ru) %{_datadir}/%{name}/sqliteman_ru.qm

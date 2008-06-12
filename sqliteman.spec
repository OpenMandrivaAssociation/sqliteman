Summary:	Lightweigth but powerfull Sqlite3 manager
Name:		sqliteman
Version:	1.0.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Databases
URL:		http://sqliteman.sourceforge.net/
Source:		http://downloads.sourceforge.net/sqliteman/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel >= 4.3.0
BuildRequires:	qt4-database-plugin-sqlite-%{_lib}
BuildRequires:	cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The best developer's and/or admin's GUI tool for Sqlite3
in the world. No joking here (or just a bit only) - it
contains the most complette feature set of all tools available.

%prep
%setup -q

%build

cmake \
	-DCMAKE_C_FLAGS="%{optflags}" \
	-DCMAKE_CXX_FLAGS="%{optflags}" \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	    %if "%{_lib}" != "lib"
		-DLIB_SUFFIX=64 \
	    %endif
	-DQT_QMAKE_EXECUTABLE=/usr/lib/qt4/bin/qmake

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

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
%defattr(644,root,root,755)
%doc %{_datadir}/%{name}/doc/*
%attr(755,root,root) %{_bindir}/sqliteman
%{_datadir}/applications/sqliteman.desktop
%{_iconsdir}/sqliteman.png
%{_datadir}/%{name}/icons/*.png
%lang(cs) %{_datadir}/%{name}/sqliteman_cs.qm
%lang(de) %{_datadir}/%{name}/sqliteman_de.qm
%lang(en) %{_datadir}/%{name}/sqliteman_en.qm
%lang(it) %{_datadir}/%{name}/sqliteman_it.qm
%lang(pl) %{_datadir}/%{name}/sqliteman_pl.qm
%lang(ru) %{_datadir}/%{name}/sqliteman_ru.qm

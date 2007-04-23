%define _snap 20070421

Summary:	Lightweigth but powerfull Sqlite3 manager
Name:		sqliteman
Version:	0.99
Release:	%mkrel 0.%{_snap}.1
License:	GPL
Group:		Development/Databases
URL:		http://sqliteman.sourceforge.net/
Source:		http://downloads.sourceforge.net/sqliteman/%{name}-%{version}-%{_snap}.tar.gz
BuildRequires:	qt4-devel			>= 4.3.0 
BuildRequires:	qt4-database-plugin-sqlite-lib
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The best developer's and/or admin's GUI tool for Sqlite3
in the world. No joking here (or just a bit only) - it
contains the most complette feature set of all tools available.

%prep
%setup -q

%build
export QTDIR=/usr/lib/qt4/

cmake \
	-DCMAKE_C_FLAGS="%{optflags}" \
	-DCMAKE_CXX_FLAGS="%{optflags}" \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} 

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-MoreApplications-Databases" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
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
%lang(pl) %{_datadir}/%{name}/sqliteman_pl.qm
															 
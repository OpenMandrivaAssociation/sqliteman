Summary:	Lightweigth but powerfull Sqlite3 manager
Name:		sqliteman
Version:	1.2.2
Release:	4
License:	GPLv2+
Group:		Development/Databases
URL:		https://sqliteman.sourceforge.net/
Source:		http://downloads.sourceforge.net/sqliteman/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel >= 4.3.0
BuildRequires:	qt4-database-plugin-sqlite
BuildRequires:	cmake
BuildRequires:	qscintilla-qt4-devel
Requires:	qt4-database-plugin-sqlite
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
%makeinstall_std -C build

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


%changelog
* Wed Nov 23 2011 Götz Waschk <waschk@mandriva.org> 1.2.2-2mdv2012.0
+ Revision: 732759
- qscintilla rebuild

* Sat Jul 17 2010 Funda Wang <fwang@mandriva.org> 1.2.2-1mdv2011.0
+ Revision: 554502
- new version 1.2.2

* Sun Jun 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.1-1mdv2010.0
+ Revision: 383487
- update to new version 1.2.1
- fix file list

  + Jerome Martin <jmartin@mandriva.org>
    - Fixed BuildRequires/Requires for 2008.1

* Wed Nov 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.0-2mdv2009.1
+ Revision: 304485
- rebuild

* Wed Aug 06 2008 Funda Wang <fwang@mandriva.org> 1.2.0-1mdv2009.0
+ Revision: 264718
- New version 1.2.0
- use non-arch dependencies

* Sun Jul 13 2008 Funda Wang <fwang@mandriva.org> 1.0.1-2mdv2009.0
+ Revision: 234232
- add requires on qt4-sqlite

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 31 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 160882
- new version
- fix file list

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-1mdv2008.0
+ Revision: 53317
- new version
- drop X-MandrivaLinux
- drop buildrequires on desktop-file-utils
- fix file list

* Tue Apr 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.99-0.20070421.1mdv2008.0
+ Revision: 17936
- correct buildrequires
- fix building on x86_64
- Import sqliteman


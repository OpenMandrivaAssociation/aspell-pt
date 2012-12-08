%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define intname aspell6
%define intver 20110424

%define languageenglazy Portuguese
%define languagecode pt
%define lc_ctype pt_PT


Name:		aspell-%{languagecode}
Summary:	%{languageenglazy} files for aspell
Group:		System/Internationalization
Version:	0.60.0
Release:	%mkrel 3
License:	GPL
URL:		http://aspell.sourceforge.net/
# http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
Source:		http://natura.di.uminho.pt/download/sources/Dictionaries/aspell6/%{intname}.%{languagecode}-%{intver}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	aspell >= 0.60
BuildRequires:	make
Requires:	aspell >= 0.60
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Obsoletes:	ispell-pt
Provides:	ispell-pt

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.


%prep
%setup -qn %{intname}-%{lc_ctype}-%{intver}-0

%build
# don't use configure macro
./configure
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc README Copyright doc/LEIAME.txt
%{_libdir}/aspell-0.60




%changelog
* Tue May 10 2011 José Melo <ze@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 673203
- 20110424-0

* Wed Apr 06 2011 José Melo <ze@mandriva.org> 0.60.0-1
+ Revision: 650945
- fix description
- version 0.60 (20110331-0)
- packaged splited since there isnt anymore an updated archieve containing
  pt_PT and pt_BR, they now exist separated

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-12mdv2011.0
+ Revision: 603454
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-11mdv2010.1
+ Revision: 518955
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-10mdv2010.0
+ Revision: 413097
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.50.2-9mdv2009.1
+ Revision: 350088
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.50.2-8mdv2009.0
+ Revision: 220439
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.50.2-7mdv2008.1
+ Revision: 182628
- provide enchant-dictionary

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-5mdv2007.0
+ Revision: 123351
- Import aspell-pt

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.2-5mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.2-4mdk
- rebuild for new aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.2-3mdk
- allow build on ia64


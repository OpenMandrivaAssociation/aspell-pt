%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define intname aspell6
%define intver 20110424

%define languageenglazy Portuguese
%define languagecode pt
%define lc_ctype pt_PT

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Group:		System/Internationalization
Version:	0.60.0
Release:	10
License:	GPLv2
Url:		http://aspell.sourceforge.net/
# http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
Source0:	http://natura.di.uminho.pt/download/sources/Dictionaries/aspell6/%{intname}.%{languagecode}-%{intver}.tar.bz2

BuildRequires:	aspell >= 0.60
Requires:	aspell >= 0.60
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
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
%makeinstall_std

%files
%doc README Copyright doc/LEIAME.txt
%{_libdir}/aspell-0.60


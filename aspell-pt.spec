%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define languageenglazy Portuguese
%define languagecode pt
%define lc_ctype pt_PT


Name:		aspell-%{languagecode}
Summary:	%{languageenglazy} files for aspell
Group:		System/Internationalization
Version:	0.60.0
Release:	%mkrel 1
License:	GPL
URL:		http://aspell.sourceforge.net/
# http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
Source:		http://natura.di.uminho.pt/download/sources/Dictionaries/aspell6/LATEST/aspell6.%{languagecode}-latest.tar.bz2
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
%setup -qn aspell6-pt_PT-20110331-0

%build
# don't use configure macro
./configure
%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Copyright
%{_libdir}/aspell-0.60



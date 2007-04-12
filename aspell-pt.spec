%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-2

%define languageenglazy Portuguese
%define languagecode pt
%define lc_ctype pt_PT

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.50.2
Release:       %mkrel 5
Group:         System/Internationalization
Source:	       http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:		   http://aspell.sourceforge.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandrake Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}
Obsoletes:	   ispell-pt
Provides:	   ispell-pt

# provides pt_BR too
Provides:	   aspell-pt_BR
Obsoletes:	   ispell-pt_BR
Provides:	   ispell-pt_BR

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.
Provides both European and Brazilian spellings

%prep
%setup -q -n %{name}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

cp doc/README README.%{languagecode}
chmod 644 README Copyright README.%{languagecode}

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.%{languagecode} Copyright
%{_libdir}/aspell-*/*



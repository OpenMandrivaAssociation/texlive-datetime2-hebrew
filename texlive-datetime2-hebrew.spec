Name:		texlive-datetime2-hebrew
Version:	47534
Release:	1
Summary:	Hebrew language module for the datetime2 package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-hebrew
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-hebrew.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-hebrew.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-hebrew.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This module provides the "hebrew" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/datetime2-hebrew
%{_texmfdistdir}/tex/latex/datetime2-hebrew
%doc %{_texmfdistdir}/doc/latex/datetime2-hebrew

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

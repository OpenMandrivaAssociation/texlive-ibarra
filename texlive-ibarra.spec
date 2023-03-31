Name:		texlive-ibarra
Version:	64567
Release:	2
Summary:	LaTeX support for the Ibarra Real Nova family of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ibarra
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibarra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ibarra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Ibarra Real Nova is a revival of a typeface designed by
Geronimo Gil for the publication of Don Quixote for the Real
Academia de la Lengua in 1780. Joaquin Ibarra was the printer.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ibarra
%{_texmfdistdir}/fonts/vf/public/ibarra
%{_texmfdistdir}/fonts/type1/public/ibarra
%{_texmfdistdir}/fonts/tfm/public/ibarra
%{_texmfdistdir}/fonts/opentype/public/ibarra
%{_texmfdistdir}/fonts/map/dvips/ibarra
%{_texmfdistdir}/fonts/enc/dvips/ibarra
%doc %{_texmfdistdir}/doc/fonts/ibarra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

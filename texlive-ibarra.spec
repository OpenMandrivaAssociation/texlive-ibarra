%global tl_name ibarra
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX support for the Ibarra Real Nova family of fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ibarra
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ibarra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ibarra.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The Ibarra Real Nova is a revival of a typeface designed by Geronimo Gil
for the publication of Don Quixote for the Real Academia de la Lengua in
1780. Joaquin Ibarra was the printer.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from ibarra:
Map ibarra.map
TL_DROPIN_EOF

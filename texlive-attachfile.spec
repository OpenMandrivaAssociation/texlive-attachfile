Name:		texlive-attachfile
Version:	v1.5b
Release:	1
Summary:	Attach arbitrary files to a PDF document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/attachfile
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Starting with PDF 1.3 (Adobe Acrobat 4.0), PDF files can
contain file attachments -- arbitrary files that a reader can
extract, just like attachments to an e-mail message. The
attachfile package brings this functionality to pdfLaTeX and
provides some additional features not available in Acrobat,
such as the ability to use arbitrary LaTeX code for the file
icon -- including things like \includegraphics, tabular, and
mathematics. Settings can be made either globally or on a per-
attachment basis. Attachfile makes it easy to attach files and
customize their appearance in the enclosing document. The
package supports the Created, Modified, and Size keys in the
EmbeddedFile's Params dictionary.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/attachfile/attachfile.sty
%doc %{_texmfdistdir}/doc/latex/attachfile/README
%doc %{_texmfdistdir}/doc/latex/attachfile/attachfile.pdf
#- source
%doc %{_texmfdistdir}/source/latex/attachfile/attachfile.dtx
%doc %{_texmfdistdir}/source/latex/attachfile/attachfile.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

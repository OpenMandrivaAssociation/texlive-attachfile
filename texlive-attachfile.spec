# revision 21866
# category Package
# catalog-ctan /macros/latex/contrib/attachfile
# catalog-date 2011-03-28 07:44:29 +0200
# catalog-license lppl1.3
# catalog-version v1.5b
Name:		texlive-attachfile
Version:	v1.5b
Release:	8
Summary:	Attach arbitrary files to a PDF document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/attachfile
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.5b-2
+ Revision: 749389
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.5b-1
+ Revision: 717866
- texlive-attachfile
- texlive-attachfile
- texlive-attachfile
- texlive-attachfile
- texlive-attachfile


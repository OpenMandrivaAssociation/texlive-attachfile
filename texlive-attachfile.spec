%global tl_name attachfile
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9
Release:	%{tl_revision}.1
Summary:	Attach arbitrary files to a PDF document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/attachfile
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/attachfile.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Starting with PDF 1.3 (Adobe Acrobat 4.0), PDF files can contain file
attachments -- arbitrary files that a reader can extract, just like
attachments to an e-mail message. The attachfile package brings this
functionality to pdfLaTeX and provides some additional features not
available in Acrobat, such as the ability to use arbitrary LaTeX code
for the file icon -- including things like \includegraphics, tabular,
and mathematics. Settings can be made either globally or on a per-
attachment basis. Attachfile makes it easy to attach files and customize
their appearance in the enclosing document. The package supports the
Created, Modified, and Size keys in the EmbeddedFile's Params
dictionary.


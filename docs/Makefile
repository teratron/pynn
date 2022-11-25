# Makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
#help:
#	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

#.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
#%: Makefile
#	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean: ## clean
	@rm -rf $(BUILDDIR)/

build-html: clean ## build html
	@$(SPHINXBUILD) -b html $(SOURCEDIR)/ $(BUILDDIR)/html

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext

all:	html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@# FIXME: Remove this `cp` once HTML->Sphinx transition is completed.
	@# Kind of a hack, but HTML-formatted docs are on the way out anyway.
	@echo "Copying legacy HTML-formatted docs into $(BUILDDIR)/html"
	@cp -a *.html tutorial $(BUILDDIR)/html
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/llvm.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/llvm.qhc"

devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/llvm"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/llvm"
	@echo "# devhelp"

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

texinfo:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."
	@echo "Run \`make' in that directory to run these through makeinfo" \
	      "(use \`make info' here to do that automatically)."

info:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo "Running Texinfo files through makeinfo..."
	make -C $(BUILDDIR)/texinfo info
	@echo "makeinfo finished; the Info files are in $(BUILDDIR)/texinfo."

gettext:
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

#--------------------------------------------------------------------------------
LATEX-BW      = $(BUILDDIR)/latex-bw
LATEX-NAME = music-for-geeks-and-nerds

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
SAMPLEOPTS = -D html_theme=sample

PAPEROPTS = -D latex_elements.pointsize=11pt -D latex_elements.preamble=\\usepackage{mfgan-bw} -D pygments_style=bw -D black_and_white=True -D code_example_wrap=67 -D latex_show_pagerefs=True

SCREENOPTS = -D latex_elements.pointsize=12pt -D latex_elements.classoptions=,openany,oneside -D latex_elements.preamble=\\usepackage{mfgan} -D pygments_style=my_pygment_style.BookStyle -D code_example_wrap=67

MOBIOPTS = -D pygments_style=none
MOBI_NAME = MusicforGeeksandNerds.mobi

# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: default view clean html epub mobi latex pdf pdf-bw text

default: html

all: html epub mobi pdf pdf-bw sample

view:
	open build/html/index.html

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html

epub:
	$(SPHINXBUILD) -b epub2 $(ALLSPHINXOPTS) $(BUILDDIR)/epub

mobi:
	$(SPHINXBUILD) -b mobi -t mobi $(MOBIOPTS) $(ALLSPHINXOPTS) $(BUILDDIR)/mobi
#	cd $(BUILDDIR)/mobi && kindlegen content.opf -o $(MOBI_NAME)

kindle-sync:
	cp $(BUILDDIR)/mobi/$(MOBI_NAME) /Volumes/Kindle/documents/
	diskutil eject /Volumes/Kindle/

latex:
	$(SPHINXBUILD) -b latex $(SCREENOPTS) $(ALLSPHINXOPTS) $(BUILDDIR)/latex

pdf:
	$(SPHINXBUILD) -b latex $(SCREENOPTS) $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	sed -i .bak -f process-latex $(BUILDDIR)/latex/$(LATEX-NAME).tex
	rsync -a latex/ $(BUILDDIR)/latex/
	$(MAKE) -C $(BUILDDIR)/latex pdf

pdf-bw:
	$(SPHINXBUILD) -b latex -t black_and_white $(PAPEROPTS) $(ALLSPHINXOPTS) $(LATEX-BW)
	sed -i .bak -f process-latex $(LATEX-BW)/$(LATEX-NAME).tex
	sed -i .bak '/\\setcounter{page}{1}/d' $(LATEX-BW)/sphinxmanual.cls
	rsync -a latex/ $(LATEX-BW)/
	$(MAKE) -C $(LATEX-BW)/ pdf

sample:
	$(SPHINXBUILD) -b latex -t sample $(SCREENOPTS) $(ALLSPHINXOPTS) $(BUILDDIR)/sample
	sed -i .bak -f process-latex $(BUILDDIR)/sample/$(LATEX-NAME).tex
	rsync -a latex/ $(BUILDDIR)/sample/
	cp figs-pdf/stamp*.pdf $(BUILDDIR)/sample/
	$(MAKE) -C $(BUILDDIR)/sample pdf
	# chapter 1, 3, 5
	pdftk A=$(BUILDDIR)/sample/$(LATEX-NAME).pdf cat A1-6 A21-25 A45-48 A84 output $(BUILDDIR)/sample/$(LATEX-NAME)-sample.pdf
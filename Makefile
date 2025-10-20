init-md:
	trestle author catalog-generate -n ex-cat -o md_ex-cat
	trestle author profile-generate -n ex-prof -o md_ex-prof
	trestle author component-generate -n ex-cd  -o md_ex-cd
	trestle author ssp-generate -cd ex-cd -p ex-prof -o md_ex-ssp -y assets/extra-ssp-meta.yml -fo
	python -m insert_response_prose

update-oscal:
	trestle author catalog-assemble -m md_ex-cat -o ex-cat
	trestle author profile-assemble -m md_ex-prof -o ex-prof
	trestle author component-assemble -m md_ex-cd -o ex-cd
	trestle author ssp-assemble -m md_ex-ssp -cd ex-cd -o ex-ssp

update-md: update-oscal
	trestle author catalog-generate -n ex-cat -o md_ex-cat
	trestle author profile-generate -n ex-prof -o md_ex-prof -y assets/extra-prof-meta.yml
	trestle author component-generate -n ex-cd  -o md_ex-cd
	trestle author ssp-generate -cd ex-cd -p ex-prof -o md_ex-ssp -y assets/extra-ssp-meta.yml -fo

ssp-md: update-md
	trestle author jinja -i ex_platform_ssp.md.jinja -ssp ex-ssp -p ex-prof -o ex_platform_ssp.md -bf "[.]" -vap "Ex Assigned:" -vnap "Assignment:"

ssp-word: ssp-md
	pandoc ex_platform_ssp.md --from markdown+table_captions+implicit_figures+rebase_relative_paths -t docx --reference-doc ssp_word_template-ex.docx -s --toc -o ex_platform_ssp.docx

clean:
	rm -rf md_*
#rm -rf component-definitions/ex-cd
	rm -rf system-security-plans/ex_ssp
#rm -f ex_platform_ssp.md ex_platform_ssp.docx

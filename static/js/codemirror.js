import { defaultKeymap, history, historyKeymap,
         insertTab } from '@codemirror/commands';
import { LanguageSupport, StreamLanguage,
         syntaxHighlighting } from '@codemirror/language';
import { Compartment, EditorState } from '@codemirror/state';
import { EditorView, keymap, lineNumbers } from '@codemirror/view';

import { oneDarkTheme, oneDarkHighlightStyle } from '@codemirror/theme-one-dark';

import { cpp } from '@codemirror/lang-cpp';
import { java } from '@codemirror/lang-java';
import { pythonLanguage } from '@codemirror/lang-python';
import { ruby } from '@codemirror/legacy-modes/mode/ruby';

const langHighlights = {
    'C': cpp(),
    'C++': cpp(),
    'Java': java(),
    'Python 3': new LanguageSupport(pythonLanguage),
    'Ruby': StreamLanguage.define(ruby)
};

/* CodeMirror editor */
(function() {
    function createEditor(textarea) {
        const langSelect = document.getElementsByClassName('submit-language')[0];
        const lang = langSelect.options[langSelect.selectedIndex].text;

        const langCompartment = new Compartment();

        const view = new EditorView({
            state: EditorState.create({
                doc: textarea.value,
                extensions: [
                    history(),
                    lineNumbers(),
                    oneDarkTheme,
                    syntaxHighlighting(oneDarkHighlightStyle),
                    keymap.of([
                        ...historyKeymap,
                        { key: 'Tab', run: insertTab }
                    ]),
                    langCompartment.of(langHighlights[lang] || [])
                ]
            })
        });

        langSelect.onchange = (e) => {
            const lang = e.target.options[e.target.selectedIndex].text;
            view.dispatch({
                effects: langCompartment.reconfigure(langHighlights[lang])
            });
        };

        textarea.parentNode.insertBefore(view.dom, textarea);
        textarea.style['display'] = 'none';

        const submitBtn = document.getElementsByClassName('submit-button')[0];

        submitBtn.addEventListener('click', () => {
            textarea.value = view.state.doc.toString();
        });
    }

    window.addEventListener('DOMContentLoaded', () => {
        const textarea = document.getElementsByClassName('codemirror-widget')[0];
        createEditor(textarea);
    });
})();

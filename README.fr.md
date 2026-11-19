# Luc Illusie, *Complexe cotangent et déformations* I–II

[English version](README.md)

Éditions LaTeX modifiables de *Complexe cotangent et déformations I* et *II* de Luc Illusie (Lecture Notes in
Mathematics 239 et 283, Springer-Verlag, 1971 et 1972), l'ouvrage qui a fondé la théorie du complexe cotangent et
son emploi en théorie des déformations.

## Lire et télécharger

Chaque édition comprend un PDF, son fichier LaTeX complet et une archive ZIP de ses sources :

| | Français, corrigé | Anglais | Français, diplomatique |
|---|---|---|---|
| Volume I | [PDF][01] · [LaTeX][02] · [sources][03] | [PDF][04] · [LaTeX][05] · [sources][06] | [PDF][16] · [LaTeX][07] · [sources][08] |
| Volume II | [PDF][09] · [LaTeX][10] | [PDF][13] · [LaTeX][14] | [PDF][11] · [LaTeX][12] |

Les trois éditions du volume II partagent une même [archive de sources][15]. Les fichiers du volume I se trouvent dans la publication
[check-2026-11-19](https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/tag/check-2026-11-19), ceux du volume II dans [pdf-check-2026-11-15](https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/tag/pdf-check-2026-11-15), et le
dossier `tex/` de ce dépôt contient les mêmes fichiers LaTeX.

- L'édition **diplomatique** reproduit le texte imprimé tel quel, coquilles comprises.
- L'édition **corrigée** corrige les coquilles évidentes de l'impression.
- L'**anglais** est une traduction du français.

Le texte, les formules et les diagrammes sont en LaTeX (les diagrammes en TikZ), et non en images de pages.

## Fabrication

La transcription, les corrections et la traduction anglaise ont été produites par IA avec OpenAI Codex :
principalement GPT-5.6 Sol (effort Ultra), certaines parties par GPT-6 Astra (effort Ultra), en août et septembre 2026.

## Qualité

Les 18 et 19 novembre 2026, GPT-6 Astra (mode Pro de ChatGPT) a contrôlé le volume I sur la numérisation du volume
imprimé (Lecture Notes in Mathematics 239), page par page dans les trois couches : le français diplomatique sur
l'imprimé, le français corrigé et ses corrections, l'anglais sur le français corrigé. **Les pages liminaires et les
pages imprimées 1 à 188 sont contrôlées** (sur 355) ; les errata de l'auteur pour les p. 11, 60 et 87 sont appliqués.
Il a relevé 7 230 modifications (diplomatique 2 224, corrigé 2 526, anglais 2 470, compilation 10), dont 130 coquilles
de l'original, corrigées dans le français corrigé. La seconde lecture de ces modifications, les pages 189 à 355, le
reste des errata et les notes sont à venir ; le volume II n'est pas encore contrôlé. Les relevés sont dans
[raw/check-2026-11-18](raw/check-2026-11-18) ; le point de sauvegarde complet est joint à la publication.

Le LaTeX de ce point de sauvegarde ne compilait pas. Claude (Claude Opus 5.5, effort high) l'a réparé par script, en ne
touchant qu'à la composition, en 23 endroits (commandes accolées à la lettre suivante, et une macro de formule centrée
employée hors de sa portée), chacun consigné dans
[REPAIR_LOG.tsv](raw/check-2026-11-18/build-repair-2026-11-19/REPAIR_LOG.tsv) ; aucune leçon n'a été changée. Les
trois éditions du volume I compilent avec LuaLaTeX, deux passes, sans erreur et sans rien qui déborde dans la marge
(pour une page de l'anglais, l'espacement des paragraphes de la compilation a reçu un peu plus de
souplesse). Claude a comparé deux corrections du contrôle à la numérisation (p. 149, « h = fp = qg » ; p. 169,
Exal_A(P, Ω_{P/A})) : toutes deux sont conformes au relevé. Le français diplomatique du volume I a maintenant aussi un
[PDF][16].

Le 6 novembre 2026, Claude (Anthropic, Claude Opus 5.5) a comparé ligne à ligne trois pages avec les volumes
imprimés : les pages 13 et 35 du volume I et la page 155 du volume II en français diplomatique, ainsi que l'anglais
de la page 13 du volume I.

- Le texte, les formules et les sept diagrammes commutatifs de ces pages sont conformes à l'imprimé.
- Le français diplomatique s'écarte de l'imprimé en trois petits points : un alinéa ajouté au milieu d'une phrase
  (I, p. 13) ; la ponctuation après trois diagrammes centrés omise (I, p. 35) ; la coquille imprimée
  « homormorphisme » rendue par « homomorphisme » (II, p. 155).
- L'anglais de I, p. 13 est exact et corrige un indice fautif de sa dernière formule (Y′ → Y′ pour Y → Y′).

Trois pages forment un petit échantillon, et il reste d'autres erreurs. Merci de les signaler par une issue GitHub.

## À propos de cette édition

Les articles de revue de Luc Illusie sont en libre accès sur Numdam, qui publie avec l'accord des revues, écrit aux
auteurs vivants et retire l'article d'un auteur qui refuse. Nous y voyons l'indication que Luc Illusie pourrait ne pas
s'opposer à cette édition, mais nous pouvons nous tromper. Nous avons écrit à l'auteur en octobre 2026 et n'avons pas
reçu de réponse.

## Droits

Les droits sur l'œuvre originale appartiennent à son auteur ou à ses représentants ou ayants droit. Notre transcription, notre traduction, nos corrections et notre composition ont été produites par IA. Elles n'ont pas d'auteur humain et, selon notre compréhension, ne sont pas protégées par le droit d'auteur ; là où un droit nous appartiendrait malgré tout, il est versé au domaine public sous CC0 1.0. Tout ce travail reproduit ou traduit l'œuvre originale : rien ici n'accorde de licence ni n'autorise une reproduction, une traduction ou un autre usage de cette œuvre. Cette édition est publiée à des fins éducatives et non lucratives, et nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici, veuillez ouvrir une issue GitHub et nous la retirerons.

[01]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/01-volume-I-francais-corrige.pdf
[02]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/02-volume-I-francais-corrige.tex
[03]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/03-volume-I-francais-corrige-sources.zip
[04]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/04-volume-I-english.pdf
[05]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/05-volume-I-english.tex
[06]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/06-volume-I-english-sources.zip
[07]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/07-volume-I-francais-diplomatique.tex
[08]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/08-volume-I-francais-diplomatique-sources.zip
[09]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/editions-2026-11-06/09-volume-II-francais-corrige.pdf
[10]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/editions-2026-11-06/10-volume-II-francais-corrige.tex
[11]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/editions-2026-11-06/11-volume-II-francais-diplomatique.pdf
[12]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/editions-2026-11-06/12-volume-II-francais-diplomatique.tex
[13]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/editions-2026-11-06/13-volume-II-english.pdf
[14]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/editions-2026-11-06/14-volume-II-english.tex
[15]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/editions-2026-11-06/15-volume-II-sources-completes.zip
[16]: https://github.com/KokunoYumeto/illusie-cotangent-complex-editions/releases/download/check-2026-11-19/16-volume-I-francais-diplomatique.pdf

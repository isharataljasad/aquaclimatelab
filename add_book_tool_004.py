from pathlib import Path
import re, zipfile, os, shutil
root = Path('/mnt/data/site_v24_work')
html_path = root/'career-os.html'
text = html_path.read_text(encoding='utf-8')

def extract_article(s, article_id):
    marker = f'<article class="card module-card" id="{article_id}">'
    start = s.find(marker)
    if start == -1:
        raise ValueError(f'not found {article_id}')
    # include indentation before marker on line
    line_start = s.rfind('\n', 0, start) + 1
    i = start
    depth = 0
    while True:
        next_open = s.find('<article', i)
        next_close = s.find('</article>', i)
        if next_close == -1:
            raise ValueError('no close')
        if next_open != -1 and next_open < next_close:
            depth += 1
            i = next_open + len('<article')
        else:
            depth -= 1
            i = next_close + len('</article>')
            if depth == 0:
                end = i
                # include trailing whitespace/newlines after article but not next section marker
                while end < len(s) and s[end] in ' \t\r\n':
                    end += 1
                return s[line_start:end], s[:line_start] + s[end:]

# Remove misplaced book tools 002 and 003, if present.
blocks = []
for bid in ['book-tool-002','book-tool-003']:
    block, text = extract_article(text, bid)
    blocks.append(block.strip())

book004 = r'''
        <article class="card module-card" id="book-tool-004">
          <div class="module-head">
            <span class="module-no">BOOK TOOL 004 · NEGOTIATION EMPATHY FRAMEWORK</span>
            <h3>إطار التفاوض بالتعاطف: عدة المحادثات الصعبة وضمان التنفيذ</h3>
            <span class="module-en">Never Split the Difference · Chris Voss with Tahl Raz · 2016</span>
            <p class="module-why">الاستخلاص المهني من الكتاب: لا نستخدم التفاوض كضغط أو مناورة، بل كطريقة إنصات وتعاطف عملي لفهم الاعتراضات، تهدئة التوتر، طرح أسئلة أقوى، والوصول إلى تنفيذ واضح بعد الاتفاق. هذه الوحدة مناسبة لاجتماعات الفريق، المحادثات الفردية، الاعتراضات، ومتابعة القرارات.</p>
          </div>

          <div class="toolbox-grid">
            <article class="toolbox-card"><span class="decision-badge">01 · LISTEN</span><h4>الاستماع قبل الرد</h4><p>نبدأ المحادثة بهدف فهم ما يقال قبل صياغة الحل أو الدفاع عن الرأي.</p><ul class="toolbox-list"><li>First Listening Protocol</li><li>سؤال مفتوح + 3 دقائق دون مقاطعة</li><li>دليل: سجل لقاءات فردية لأربعة أسابيع</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">02 · MIRROR</span><h4>المرآة اللفظية</h4><p>تكرار آخر كلمتين أو ثلاث بنبرة هادئة يفتح المجال لتوضيح أعمق.</p><ul class="toolbox-list"><li>Verbal Mirror Card</li><li>كرر، اصمت، دوّن ما ظهر</li><li>دليل: 5 محادثات موثقة</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">03 · LABEL</span><h4>تسمية التوتر</h4><p>عندما يظهر قلق أو تردد، نسمّيه بلغة محايدة بدل تجاهله أو مقاومته.</p><ul class="toolbox-list"><li>Meeting Labeling Log</li><li>يبدو أن... / أحس أن...</li><li>دليل: 6 حالات خلال 30 يومًا</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">04 · NO</span><h4>وضوح الاعتراض</h4><p>الرفض الواضح أفضل من موافقة شكلية؛ نطلب التحفظات حتى نحسن القرار.</p><ul class="toolbox-list"><li>Clear Task Assignment Template</li><li>ما الذي لا يصلح في هذا الطرح؟</li><li>دليل: 4 تكليفات مع اعتراضات وحلول</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">05 · CONFIRM</span><h4>ملخص تأكيدي</h4><p>لا نكتفي بالموافقة؛ نلخص ما سمعناه حتى يصحح الطرف الآخر الفهم.</p><ul class="toolbox-list"><li>Summary Confirmation Protocol</li><li>إذن ما تقوله هو...</li><li>دليل: ملخصات مؤرخة ومصححة</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">06 · QUESTIONS</span><h4>الأسئلة المعيارية</h4><p>أسئلة ماذا وكيف تقلل الدفاعية وتدفع الفريق للمشاركة في الحل.</p><ul class="toolbox-list"><li>Calibrated Question Bank</li><li>15–20 سؤالًا للفريق</li><li>دليل: 3 اجتماعات حل مشكلات</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">07 · EXECUTE</span><h4>ضمان التنفيذ</h4><p>الاتفاق لا يكفي. نسأل كيف سننفذ؟ كيف نعرف أننا على المسار؟ وماذا عند العائق؟</p><ul class="toolbox-list"><li>Execution Confirmation Log</li><li>خطوات، مالك، موعد، مراجعة</li><li>دليل: 4 قرارات جماعية موثقة</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">08 · STYLE</span><h4>أنماط التفاوض كوعي ذاتي</h4><p>نلاحظ أسلوبنا في المحادثة دون تصنيف الناس أو ادعاء قياس نفسي.</p><ul class="toolbox-list"><li>Team Communication Style Card</li><li>حازم / محاور / محلل كملاحظة عمل</li><li>دليل: خريطة تواصل آمنة</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">09 · RISK</span><h4>توضيح مخاطر التأخير</h4><p>نشرح أثر عدم التنفيذ دون ضغط شخصي: ماذا سيحدث لو لم نتحرك؟</p><ul class="toolbox-list"><li>Project Risk Clarification Sheet</li><li>أثر التأخير + عائق التنفيذ</li><li>دليل: مشروعان مع خطة متابعة</li></ul></article>
            <article class="toolbox-card"><span class="decision-badge">10 · DISCOVER</span><h4>استكشاف غير المصرح به</h4><p>قبل القرار نسأل: ما الذي لم نتحدث عنه وقد يؤثر في النتيجة؟</p><ul class="toolbox-list"><li>Unknowns Discovery Checklist</li><li>ما أعرفه / ما لا أعرفه / سؤال غير مباشر</li><li>دليل: 3 قرارات سبقتها ورقة استكشاف</li></ul></article>
          </div>

          <div class="module-body" style="margin-top:28px">
            <details open>
              <summary>الأدوات الست الجاهزة <span class="sum-tag">READY TO USE</span></summary>
              <div class="mod-content">
                <div class="table-wrap">
                  <table class="decision-table">
                    <thead><tr><th scope="col">الأداة</th><th scope="col">استخدامها في 10 دقائق</th><th scope="col">الدليل الناتج</th></tr></thead>
                    <tbody>
                      <tr><td><strong>Weekly One-on-One Protocol</strong></td><td>سؤال افتتاحي، استماع دون مقاطعة، نقطتان مسموعتان، ملخص بصوت عال، وسؤال كيف لضمان التنفيذ.</td><td>ورقة اجتماع فردي تتضمن ملخصًا مؤكدًا ونقطة مراجعة.</td></tr>
                      <tr><td><strong>Calibrated Question Bank</strong></td><td>اختر أسئلة ماذا/كيف لفهم الوضع، ضمان التنفيذ، أو اكتشاف المجهول.</td><td>بنك أسئلة مخصص للفريق مع مواقف الاستخدام.</td></tr>
                      <tr><td><strong>Execution Confirmation Log</strong></td><td>بعد كل قرار: الخطوات، المسؤول، الموعد، كيف نعرف أننا على المسار، وماذا نفعل عند العائق.</td><td>سجل قرار جماعي قابل للمتابعة.</td></tr>
                      <tr><td><strong>Team Communication Style Card</strong></td><td>لاحظ أنماط التواصل كطريقة عمل فقط: مباشر، محاور، محلل؛ ثم عدّل أسلوبك دون تصنيف نفسي.</td><td>خريطة تواصل آمنة للفريق.</td></tr>
                      <tr><td><strong>Unknowns Discovery Checklist</strong></td><td>قبل القرار: اكتب ما تعرفه، ما تعرف أنك لا تعرفه، وما قد يكون موجودًا ولم تسأل عنه.</td><td>ورقة استكشاف قبل القرارات المهمة.</td></tr>
                      <tr><td><strong>30-Day Practice Log</strong></td><td>سجل يوميًا الموقف، الأداة المستخدمة، ما حدث، وملاحظة تطوير واحدة.</td><td>سجل ممارسة يومي يربط الأداة بالدليل.</td></tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </details>
            <details>
              <summary>خطة ممارسة 30 يومًا <span class="sum-tag">30-DAY PRACTICE</span></summary>
              <div class="mod-content">
                <ul class="compact-list">
                  <li><strong>الأسبوع 1 — الاستماع والمرآة:</strong> طبق بروتوكول الاستماع في 3 لقاءات، وجرب المرآة في محادثتين. المخرج: أوراق ملاحظات مكتوبة.</li>
                  <li><strong>الأسبوع 2 — التسمية والأسئلة:</strong> استخدم عبارات تسمية محايدة، وابنِ بنك أسئلة من 15 سؤالًا. المخرج: بنك أسئلة + سجل 6 حالات.</li>
                  <li><strong>الأسبوع 3 — التنفيذ والمتابعة:</strong> طبق سجل تأكيد التنفيذ بعد القرارات، وأكمل خريطة تواصل الفريق. المخرج: نموذجا تأكيد تنفيذ + خريطة تواصل.</li>
                  <li><strong>الأسبوع 4 — التوليف والتوثيق:</strong> طبق الأدوات في موقف مهني واحد، واستخدم قائمة استكشاف المجهول قبل قرار مهم، ثم اكتب تقرير صفحة واحدة.</li>
                </ul>
              </div>
            </details>
            <details>
              <summary>قالب تقرير صفحة واحدة <span class="sum-tag">ONE-PAGE REPORT</span></summary>
              <div class="mod-content">
                <ol class="report-template">
                  <li><strong>الأدوات المطبقة:</strong> الاستماع الأول، المرآة، التسمية، بنك الأسئلة، تأكيد التنفيذ، خريطة التواصل، أو استكشاف المجهول.</li>
                  <li><strong>الآثار المنتجة:</strong> أوراق لقاءات فردية، بنك أسئلة، سجلات تسمية، نماذج تنفيذ، أو أوراق استكشاف.</li>
                  <li><strong>دليل الجاهزية:</strong> عدد الاجتماعات الفردية، القرارات الجماعية، المحادثات الصعبة، والمواقف التي احتاجت تفاوضًا داخليًا.</li>
                  <li><strong>ملاحظة التطوير:</strong> سلوك واحد سيستمر وسلوك واحد يحتاج تحسينًا.</li>
                  <li><strong>حدود التقرير:</strong> توثيق ممارسة ذاتية وليس شهادة تفاوض أو ضمان نتيجة أو تقييمًا رسميًا للأشخاص.</li>
                </ol>
              </div>
            </details>
            <details>
              <summary>جملة سيرة وLinkedIn آمنة <span class="sum-tag">SAFE WORDING</span></summary>
              <div class="mod-content">
                <div class="cv-snippet">Built a 30-day negotiation-empathy practice framework, organized practical tools including structured listening protocols, calibrated question banks, and execution-confirmation templates, and documented measurable readiness evidence across team leadership interactions.</div>
                <p><strong>LinkedIn:</strong> طورت إطارًا تطبيقيًا مستخلصًا من مبادئ التفاوض القائم على التعاطف، وبنيت أدوات موثقة للاستماع الفعال وصياغة الأسئلة وضمان التنفيذ، مع تسجيل أدلة قابلة للقياس عبر تطبيق ميداني امتد 30 يومًا في سياق قيادة الفريق.</p>
                <p><strong>بيان الأمان:</strong> هذه الأدوات لا تنقل أمثلة الكتاب الحساسة، ولا تستخدم التفاوض للتلاعب، ولا تدّعي شهادة أو إتقانًا. هي قوالب إنصات وأسئلة ومتابعة تساعد على محادثات أوضح وقرارات قابلة للتنفيذ.</p>
              </div>
            </details>
          </div>
        </article>
'''

# Insert moved 002, 003 and new 004 inside the book-derived section, before its original closing div/section after book-tool-001.
# After removing 002 and 003, the section closes immediately after book-tool-001. Replace that closure.
closure = '        </article>\n      </div>\n    </section>\n\n<section class="section" id="skill-modules">'
pos = text.find(closure)
if pos == -1:
    raise ValueError('book-derived closure not found')
replacement = '        </article>\n\n' + '\n\n'.join(blocks) + '\n\n' + book004 + '\n      </div>\n    </section>\n\n<section class="section" id="skill-modules">'
text = text.replace(closure, replacement, 1)

# Update meta description/title lightly
text = text.replace('ومشاريع توفير وتحسين آمنة.', 'ومشاريع توفير وتحسين آمنة، وأدوات قيادة مستخلصة من كتب.', 1)
html_path.write_text(text, encoding='utf-8')

# Update index homepage text/card
idx_path = root/'index.html'
idx = idx_path.read_text(encoding='utf-8')
idx = idx.replace('وأضيف الآن مسار أدوات الكتب مع Book Tool 001 للثقة كأفعال صغيرة، وBook Tool 002 لتصفية الذهن وحماية التركيز، وBook Tool 003 لأنماط التفاعل كعدة تواصل وإسناد.', 'وأضيف الآن مسار أدوات الكتب مع Book Tool 001 للثقة كأفعال صغيرة، وBook Tool 002 لتصفية الذهن وحماية التركيز، وBook Tool 003 لأنماط التفاعل كعدة تواصل وإسناد، وBook Tool 004 للتفاوض بالتعاطف وضمان التنفيذ.')
idx = idx.replace('Confidence + Clear-Mind + Interaction Styles', 'Confidence + Clear-Mind + Interaction + Negotiation')
idx = idx.replace('تحويل الكتب إلى أدوات عمل: بطاقة اجتماع، مواءمة توقعات، مصفوفة فرز، مراجعة أسبوعية، بروتوكول إصغاء، وقرار إسناد وتخطيط تواصل.', 'تحويل الكتب إلى أدوات عمل: بطاقة اجتماع، مواءمة توقعات، مصفوفة فرز، مراجعة أسبوعية، تخطيط تواصل، قرار إسناد، وأسئلة تفاوض تضمن التنفيذ.')
idx_path.write_text(idx, encoding='utf-8')

# Add Claude prompt
prompt = '''You are continuing the existing static website ZIP:
AquaClimate Lab × إشارات الجسد
Career-OS Toolbox | Book-Derived Leadership Tools

Current source of truth:
aquaclimatelab_site_v24_book_tool_004_negotiation_empathy.zip

Final polish only. Do not restart the site. Do not convert to React, Next.js, Astro, Vue, or any framework. Static HTML + CSS + JS only.

Newly added section:
Book Tool 004 — Negotiation Empathy Framework
إطار التفاوض بالتعاطف: عدة المحادثات الصعبة وضمان التنفيذ
Source: Never Split the Difference, Chris Voss with Tahl Raz, 2016.

Important editorial rules:
- Do not summarize the book normally.
- Do not copy long book passages.
- Do not include hostage-negotiation examples or manipulative wording.
- Keep it as practical workplace tools for team leadership: listening, calibrated questions, task clarity, objections, execution follow-up, and safe evidence.
- Do not claim negotiation certification, mastery, psychological profiling, or guaranteed outcomes.
- Do not use confidential company data.
- Keep Arabic RTL clean and mobile-first.
- Keep Water Wonder, PDFs, back-to-top, and both emails intact.
- Keep blocked career-outcome wording absent.

Polish checks:
1. Book tools 001–004 render in one coherent Book-Derived Leadership Tools flow.
2. Module 004 reads as tools, not book marketing.
3. Tables scroll well on mobile.
4. Internal anchors work.
5. No broken links.
6. No blocked wording appears.

Return:
1. Ready-to-deploy ZIP.
2. Changed files summary.
3. Static HTML/CSS/JS confirmation.
4. Confirmation that Water Wonder and PDFs remain untouched.
'''
(root/'CLAUDE_FABLE_V24_BOOK_TOOL_004_PROMPT.md').write_text(prompt, encoding='utf-8')

# Changelog
ch = root/'CHANGELOG.md'
old = ch.read_text(encoding='utf-8') if ch.exists() else ''
entry = '''\n\n## v24 — Book Tool 004: Negotiation Empathy Framework\n- Added Book Tool 004 under Book-Derived Leadership Tools.\n- Converted Never Split the Difference extraction into a workplace leadership toolkit: listening, mirroring, neutral labeling, calibrated questions, execution confirmation, communication style awareness, risk clarification, and unknowns discovery.\n- Reorganized Book Tools 001–004 into one coherent section flow in career-os.html.\n- Updated homepage Book Tools teaser to include negotiation-empathy tools.\n- Added Claude Fable final-polish prompt for v24.\n- Preserved static HTML/CSS/JS structure, Water Wonder links, PDFs, and contact emails.\n'''
ch.write_text(old + entry, encoding='utf-8')

print('done')

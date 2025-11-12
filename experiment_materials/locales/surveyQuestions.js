export const surveyQuestions = {
    zh: {
        "survey2": {
            type: 'matrix',
            scaleLabels: ['非常不同意', '不太同意', '态度中立', '比较同意', '非常同意'],
            questions: [{ 'id': 0, 'text': "性格外向，喜欢交际" }, { 'id': 1, 'text': "比较安静" }, { 'id': 2, 'text': "有时会害羞，比较内向" }, { 'id': 3, 'text': "爱说话，健谈" }]

        },
        "survey4": {
            type: 'matrix',
            scaleLabels: ['完全不像我', '不像我', '不大像我', '有点像我', '像我', '非常像我'],
            questions: [{ 'id': 0, 'text': '想出新点子，发挥创意对他来说很重要。他喜欢以与众不同的方式做事。' }, { 'id': 1, 'text': '富裕对他来说很重要，他希望自己有很多很多的钱并拥有许多昂贵的东西。' }, 
                { 'id': 2, 'text': '他认为普天下人人平等很重要。他相信生活中每个人都应当享有平等的机会。' }, { 'id': 3, 'text': '对他来说，发挥自己的才能很重要。他希望以此得到人们的欣赏。' }, 
                { 'id': 4, 'text': '安全的生活环境对他来说很重要。他避免任何会危及自身安全的事情。' }, { 'id': 5, 'text': '他喜欢惊喜，总是寻求新鲜事物。他认为丰富多彩的人生经历很重要。' }, 
                { 'id': 6, 'text': '他认为人们应该懂得服从命令。在他看来，任何情况下大家都要遵守规则，即使身边没人注意。' }, 
                { 'id': 7, 'text': '聆听不同的意见对他来说很重要。即使他和别人意见不合，他仍然希望能够理解别人。' }, { 'id': 8, 'text': '恭敬和谦虚对他来说很重要。他尽量避免引起别人的注意。' }, 
                { 'id': 9, 'text': '享受生活的乐趣对他来说很重要。他喜欢让自己尽情享乐。' }, { 'id': 10, 'text': '自己的事自己做主对他来说很重要。他喜欢自由地筹划和安排，不依靠他人。' }, 
                { 'id': 11, 'text': '帮助身边的人对他来说很重要。他希望关心他们，使他们生活幸福。' }, { 'id': 12, 'text': '成功对他来说很重要。他希望别人认可他的成就。' }, 
                { 'id': 13, 'text': '国家能给他完全安全保障对他来说非常重要。他希望一个能保护人民的强壮国家。' }, { 'id': 14, 'text': '他总是寻找参与冒险的机会。希望刺激有趣的生活。' }, 
                { 'id': 15, 'text': '举止得体对他来说很重要。他不希望做出任何会引起别人非议的事情。' }, { 'id': 16, 'text': '别人对他的尊重对他来说很重要。他希望别人按他的主意办事。' }, 
                { 'id': 17, 'text': '保持对朋友忠心耿耿对他来说很重要。他希望为亲友付出一切。' }, { 'id': 18, 'text': '他坚信人们应该关爱大自然。爱护生态环境对他来说很重要。' }, 
                { 'id': 19, 'text': '传统对他很重要。他尝试按照宗教或家庭传统风俗习惯为人处世。' }, { 'id': 20, 'text': '他把握每一个开心的机会。做能给自己带来乐趣的事对他来说很重要。' }]
        },
        "survey3": {
            type: 'matrix',
            scaleLabels: ['非常不符合', '有点不符合', '有时符合有时不符合', '有点符合', '非常符合'],
            questions: [{ 'id': 0, 'text': '在做任何重要事情之前，我都会仔细计划我的行动。' }, { 'id': 1, 'text': '我经常依靠直觉行事。' }, { 'id': 2, 'text': '只要感觉对，我就觉得某种行为适合我。' }, 
                { 'id': 3, 'text': '在开始做某个任务之前，我会收集所有需要的信息。' }, { 'id': 4, 'text': '当我做一些非常重要的事情时，我会努力遵循我的工作计划。' }, 
                { 'id': 5, 'text': '我经常在对所做的事情一无所知的情况下就开始工作。' }, { 'id': 6, 'text': '我通常以系统化和有组织的方式做出决定。' },
                { 'id': 'testQuestion', 'text': '这道题请选择非常符合', 'isTestQuestion': true, 'correctAnswer': "非常符合" },
                { 'id': 7, 'text': '当我决定如何行动时，我会遵循内心的感受和情绪。' }, { 'id': 8, 'text': '当我需要在多个选项之间做选择时，我会分析每一个选项并选择最好的一个。' }, 
                { 'id': 9, 'text': '我经常在不知不觉中做出了一个好的决定。' }]
        },
        "survey1": {
            questions: [
                {
                    id: 'q1',
                    type: 'scale',
                    text: '请调整量表，表示今天您整体的情绪是愉快还是不愉快。',
                    min: 1,
                    max: 10,
                    label1: '非常沮丧',
                    label2: '有点沮丧',
                    label3: '一般',
                    label4: '比较愉快',
                    label5: '非常愉快'
                },
                {
                    id: 'q2',
                    type: 'scale',
                    text: '请调整量表，表示今天您整体的情绪是平静还是激动。',
                    min: 1,
                    max: 10,
                    label1: '非常平静',
                    label2: '有点平静',
                    label3: '一般',
                    label4: '比较激动',
                    label5: '非常激动'
                },
                {
                    id: 'q3',
                    type: 'choice',
                    text: '您如何衡量自己今天的精力水平？',
                    choices: ["没有精力或动力做很多事情",
                        "有足够的精力勉强度日，但没有足够的精力提高工作效率",
                        "精力充沛，工作效率一般",
                        "精力充沛，工作效率比平时更高",
                        "精力异常充沛，有时感觉亢奋甚至激动"
                    ]
                },
            ]
        }
    },
    en: {
        "survey2": {
            type: 'matrix',
            scaleLabels: ['Agree strongly', 'Agree a little', 'Neutral;no opinion', 'Disagree a little', 'Disagree strongly'],
            questions: [{ 'id': 0, 'text': "Is outgoing, sociable." }, { 'id': 1, 'text': "Tends to be quiet." }, { 'id': 2, 'text': "Is sometimes shy, introverted." }, { 'id': 3, 'text': "Is talkative." }]

        },
        "survey4": {
            type: 'matrix',
            scaleLabels: ['Very much like me', 'Like me', 'Somewhat like me', 'A little like me', 'Not like me', 'Not like me at all'],
            questions: [
                { 'id': 0, 'text': 'Thinking up new ideas and being creative is important to him. He likes to do things in his own original way.' },
                { 'id': 1, 'text': 'It is important to him to be rich. He wants to have a lot of money and expensive things.' },
                { 'id': 2, 'text': 'He thinks it is important that every person in the world be treated equally. He believes everyone should have equal opportunities in life.' },
                { 'id': 3, 'text': 'It is important to him to show his abilities. He wants people to admire what he does.' },
                { 'id': 4, 'text': 'It is important to him to live in secure surroundings. He avoids anything that might endanger his safety.' },
                { 'id': 5, 'text': 'He likes surprises and is always looking for new things to do. He thinks it is important to do lots of different things in life.' },
                { 'id': 6, 'text': 'He believes that people should do what they are told. He thinks people should follow rules at all times, even when no-one is watching.' },
                { 'id': 7, 'text': 'It is important to him to listen to people who are different from him. Even when he disagrees with them, he still wants to understand them.' },
                { 'id': 8, 'text': 'It is important to him to be humble and modest. He tries not to draw attention to himself.' },
                { 'id': 9, 'text': 'Having a good time is important to him. He likes to “spoil” himself.' },
                { 'id': 10, 'text': 'It is important to him to make his own decisions about what he does. He likes to be free to plan and not depend on others.' },
                { 'id': 11, 'text': 'It is very important to him to help the people around him. He wants to care for their well-being.' },
                { 'id': 12, 'text': 'Being very successful is important to him. He hopes people will recognize his achievements.' },
                { 'id': 13, 'text': 'It is important to him that the government insure his safety against all threats. He wants the state to be strong so it can defend its citizens.' },
                { 'id': 14, 'text': 'He looks for adventures and likes to take risks. He wants to have an exciting life. ' },
                { 'id': 15, 'text': 'It is important to him always to behave properly. He wants to avoid doing anything people would say is wrong.' },
                { 'id': 16, 'text': 'It is important to him to get respect from others. He wants people to do what he says.' },
                { 'id': 17, 'text': 'It is important to him to be loyal to his friends. He wants to devote himself to people close to him.' },
                { 'id': 18, 'text': 'He strongly believes that people should care for nature. Looking after the environment is important to him.' },
                { 'id': 19, 'text': 'Tradition is important to him. He tries to follow the customs handed down by his religion or his family.' },
                { 'id': 20, 'text': 'He seeks every chance he can to have fun. It is important to him to do things that give him pleasure.' }]
        },
        "survey3": {
            type: 'matrix',
            scaleLabels: ['Very correct', 'Somewhat correct', 'Sometimes correct and sometime incorrect', 'Somewhat incorrect', 'Very incorrect'],
            questions: [{ 'id': 0, 'text': 'Before I do anything important, I carefully plan my actions. ' },
            { 'id': 1, 'text': 'I often follow my instincts. ' },
            { 'id': 2, 'text': 'I know a way of conduct suits me, if I feel it’s right. ' },
            { 'id': 3, 'text': 'Before I start working on an assignment, I gather all the needed information. ' },
            { 'id': 4, 'text': 'When I do something of great importance, I make an effort to follow my working plan. ' },
            { 'id': 5, 'text': 'I often start working on an assignment with no idea of what I’m about to do. ' },
            { 'id': 6, 'text': 'I usually make decisions in a systematic and organized way. ' },
            { 'id': 'testQuestion', 'text': 'Please selsect Very correct for this question', 'isTestQuestion': true, 'correctAnswer': "Very correct" },
            { 'id': 7, 'text': 'When I decide how to act, I follow my inner feelings and emotions. ' },
            { 'id': 8, 'text': 'When I have to choose between alternatives, I analyze each of them and choose the best one. ' },
            { 'id': 9, 'text': 'I often make a good decision without really knowing how I did it.' }]
        },
        "survey1": {
            questions: [
                {
                    id: 'q1',
                    type: 'scale',
                    text: 'Please adjust the scale to indicate whether your overall mood is happy or sad today.',
                    min: 1,
                    max: 10,
                    label1: 'Very sad',
                    label2: 'Somewhat sad',
                    label3: 'Neutral',
                    label4: 'Somewhat happy',
                    label5: 'Very happy'
                },
                {
                    id: 'q2',
                    type: 'scale',
                    text: 'Please adjust the scale to indicate whether your overall mood is calm or excited today.',
                    min: 1,
                    max: 10,
                    label1: 'Very calm',
                    label2: 'Somewhat calm',
                    label3: 'Neutral',
                    label4: 'Somewhat excited',
                    label5: 'Very excited'
                },
                {
                    id: 'q3',
                    type: 'choice',
                    text: 'How would you gauge your energy level today',
                    choices: ["Little energy or motivation to do much of anything",
                        "Enough energy to get by but not enough to be very productive",
                        "Typical energy level with usual productivity",
                        "Plenty of energy to be even more productive than usual",
                        "Unusually high energy feeling hyper or even agitated at times"
                    ]
                },
            ]
        }

    }
};

export const surveyTitles = {
    zh: {
        "survey1": "【量表1/4】请您仔细阅读以下题目，评估您今天的状态。",
        "survey2": "【量表2/4】下面是一些关于个人特征的描述，有些可能适用于你，有些可能不适用于你。比如，你是否同意 “你是一个喜欢与他人待在一起的人”？请选择对应的选项以表明你同意或不同意这个描述。",
        "survey3": "【量表3/4】下面是一系列描述不同人工作风格的语句。工作风格描述了人们做出重要决定（如选择职业或租房）或执行重要任务（如撰写学术论文或计划假期）的方式。请小心阅读并仔细评估以下每一条描述与您的符合程度。",
        "survey4": "【量表4/4】下面是对一些人的简要描述。请在读完每段描述后想想被描述者和自己有多相似，然后在该描述右边选择出和自己相似的程度。",
    },
    en: {
        "survey1": "【Scale 1/4】Please read the following questions carefully to assess your mental status today.",
        "survey2": "【Scale 2/4】Here are a number of characteristics that may or may not apply to you. For example, do you agree that you are someone who likes to spend time with others? Please make your choice for each statement to indicate the extent to which you agree or disagree with that statement. I am someone who...",
        "survey3": "【Scale 3/4】Bellow is a series of statements describing working styles of various people. A working style describes the way people make an important decision (e.g., choosing an occupation or renting an apartment) or carry out an important task (e.g., writing an academic paper or planning a vacation). For each of the following statements, please indicate how well it describes you. ",
        "survey4": "【Scale 4/4】Here we briefly describe some people. Please read each description and think about how much each person is or is not like you. Tick the box to the right that shows how much the person in the description is like you",
    }
}
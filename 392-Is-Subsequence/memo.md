## Step 1

Full sequenceとSubsequenceを一文字ずつ順番に確認していき、同じものがヒットしたら、Subsequenceのポインタを一つ進める。最後まで確認して、Subsequenceのポインタが最後まで進んでいれば、SubsequenceはFull sequenceの部分列であると判断できる。
初め`ptr`が最後まで到達した時string out of rangeになることを忘れていたら、for文の中でその判定も行うようにした。

## Step 2

Step 1の解について、最後のif文判定部分は返り値ごと `ptr == len(s)` とすることで簡略化して書くことができることに気づいた。
また、イテレータとallを使うことでさらに簡略化して書けることをClaudeに教えてもらった。ただこれは視認性が悪いと思う。

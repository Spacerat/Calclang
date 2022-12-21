// Generated from /Users/josephatkins-turkish/repos/calclang/ExprParser.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SINGLE_COMMENT=1, MULTILINE_COMMENT=2, AND=3, THEN=4, OR=5, NOT=6, EQ=7, 
		COMMA=8, SEMI=9, LPAREN=10, RPAREN=11, TO=12, PLUS=13, MINUS=14, TIMES=15, 
		DIVIDE=16, LINEAR=17, GAUSSIAN=18, DAYS=19, WEEKS=20, HOURS=21, MINUTES=22, 
		INT=23, FLOAT=24, ID=25, BRACKET_ID=26, WS=27, NL=28;
	public static final int
		RULE_program = 0, RULE_terminate = 1, RULE_id = 2, RULE_stat = 3, RULE_rangeSpec = 4, 
		RULE_unit = 5, RULE_numericLiteral = 6, RULE_expr = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "terminate", "id", "stat", "rangeSpec", "unit", "numericLiteral", 
			"expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'and'", null, "'or'", "'not'", "'='", "','", "';'", 
			"'('", "')'", "'to'", "'+'", "'-'", "'*'", "'/'", "'linear'", "'gaussian'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SINGLE_COMMENT", "MULTILINE_COMMENT", "AND", "THEN", "OR", "NOT", 
			"EQ", "COMMA", "SEMI", "LPAREN", "RPAREN", "TO", "PLUS", "MINUS", "TIMES", 
			"DIVIDE", "LINEAR", "GAUSSIAN", "DAYS", "WEEKS", "HOURS", "MINUTES", 
			"INT", "FLOAT", "ID", "BRACKET_ID", "WS", "NL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ExprParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public StatContext statements;
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LPAREN) | (1L << INT) | (1L << FLOAT) | (1L << ID) | (1L << BRACKET_ID))) != 0)) {
				{
				{
				setState(16);
				((ProgramContext)_localctx).statements = stat();
				}
				}
				setState(21);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(22);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TerminateContext extends ParserRuleContext {
		public TerminalNode SEMI() { return getToken(ExprParser.SEMI, 0); }
		public TerminateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terminate; }
	}

	public final TerminateContext terminate() throws RecognitionException {
		TerminateContext _localctx = new TerminateContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_terminate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdContext extends ParserRuleContext {
		public IdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id; }
	 
		public IdContext() { }
		public void copyFrom(IdContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class RawIdContext extends IdContext {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public RawIdContext(IdContext ctx) { copyFrom(ctx); }
	}
	public static class BracketIdContext extends IdContext {
		public TerminalNode BRACKET_ID() { return getToken(ExprParser.BRACKET_ID, 0); }
		public BracketIdContext(IdContext ctx) { copyFrom(ctx); }
	}

	public final IdContext id() throws RecognitionException {
		IdContext _localctx = new IdContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_id);
		try {
			setState(28);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				_localctx = new RawIdContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				match(ID);
				}
				break;
			case BRACKET_ID:
				_localctx = new BracketIdContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				match(BRACKET_ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatContext extends ParserRuleContext {
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AssignmentContext extends StatContext {
		public IdContext target;
		public ExprContext expression;
		public TerminalNode EQ() { return getToken(ExprParser.EQ, 0); }
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminateContext terminate() {
			return getRuleContext(TerminateContext.class,0);
		}
		public AssignmentContext(StatContext ctx) { copyFrom(ctx); }
	}
	public static class StatementContext extends StatContext {
		public ExprContext expression;
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminateContext terminate() {
			return getRuleContext(TerminateContext.class,0);
		}
		public StatementContext(StatContext ctx) { copyFrom(ctx); }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_stat);
		int _la;
		try {
			setState(40);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				_localctx = new AssignmentContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(30);
				((AssignmentContext)_localctx).target = id();
				setState(31);
				match(EQ);
				setState(32);
				((AssignmentContext)_localctx).expression = expr(0);
				setState(34);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SEMI) {
					{
					setState(33);
					terminate();
					}
				}

				}
				break;
			case 2:
				_localctx = new StatementContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(36);
				((StatementContext)_localctx).expression = expr(0);
				setState(38);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SEMI) {
					{
					setState(37);
					terminate();
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RangeSpecContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(ExprParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(ExprParser.RPAREN, 0); }
		public TerminalNode LINEAR() { return getToken(ExprParser.LINEAR, 0); }
		public TerminalNode GAUSSIAN() { return getToken(ExprParser.GAUSSIAN, 0); }
		public RangeSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rangeSpec; }
	}

	public final RangeSpecContext rangeSpec() throws RecognitionException {
		RangeSpecContext _localctx = new RangeSpecContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_rangeSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(LPAREN);
			setState(43);
			_la = _input.LA(1);
			if ( !(_la==LINEAR || _la==GAUSSIAN) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(44);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnitContext extends ParserRuleContext {
		public TerminalNode WEEKS() { return getToken(ExprParser.WEEKS, 0); }
		public TerminalNode DAYS() { return getToken(ExprParser.DAYS, 0); }
		public TerminalNode HOURS() { return getToken(ExprParser.HOURS, 0); }
		public TerminalNode MINUTES() { return getToken(ExprParser.MINUTES, 0); }
		public UnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unit; }
	}

	public final UnitContext unit() throws RecognitionException {
		UnitContext _localctx = new UnitContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_unit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DAYS) | (1L << WEEKS) | (1L << HOURS) | (1L << MINUTES))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumericLiteralContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(ExprParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(ExprParser.FLOAT, 0); }
		public NumericLiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numericLiteral; }
	}

	public final NumericLiteralContext numericLiteral() throws RecognitionException {
		NumericLiteralContext _localctx = new NumericLiteralContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_numericLiteral);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ParensContext extends ExprContext {
		public TerminalNode LPAREN() { return getToken(ExprParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ExprParser.RPAREN, 0); }
		public ParensContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IdentContext extends ExprContext {
		public IdContext id() {
			return getRuleContext(IdContext.class,0);
		}
		public IdentContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class RangeContext extends ExprContext {
		public ExprContext bottom;
		public ExprContext top;
		public TerminalNode TO() { return getToken(ExprParser.TO, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public RangeSpecContext rangeSpec() {
			return getRuleContext(RangeSpecContext.class,0);
		}
		public RangeContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ValueContext extends ExprContext {
		public NumericLiteralContext value;
		public UnitContext valueUnit;
		public NumericLiteralContext numericLiteral() {
			return getRuleContext(NumericLiteralContext.class,0);
		}
		public UnitContext unit() {
			return getRuleContext(UnitContext.class,0);
		}
		public ValueContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class BinopContext extends ExprContext {
		public ExprContext lhs;
		public Token op;
		public ExprContext rhs;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode TIMES() { return getToken(ExprParser.TIMES, 0); }
		public TerminalNode DIVIDE() { return getToken(ExprParser.DIVIDE, 0); }
		public TerminalNode PLUS() { return getToken(ExprParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(ExprParser.MINUS, 0); }
		public TerminalNode AND() { return getToken(ExprParser.AND, 0); }
		public TerminalNode THEN() { return getToken(ExprParser.THEN, 0); }
		public BinopContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 14;
		enterRecursionRule(_localctx, 14, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case BRACKET_ID:
				{
				_localctx = new IdentContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(51);
				id();
				}
				break;
			case INT:
			case FLOAT:
				{
				_localctx = new ValueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(52);
				((ValueContext)_localctx).value = numericLiteral();
				setState(54);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(53);
					((ValueContext)_localctx).valueUnit = unit();
					}
					break;
				}
				}
				break;
			case LPAREN:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(56);
				match(LPAREN);
				setState(57);
				expr(0);
				setState(58);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(82);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(80);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
					case 1:
						{
						_localctx = new BinopContext(new ExprContext(_parentctx, _parentState));
						((BinopContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(62);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(63);
						((BinopContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==TIMES || _la==DIVIDE) ) {
							((BinopContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(64);
						((BinopContext)_localctx).rhs = expr(6);
						}
						break;
					case 2:
						{
						_localctx = new BinopContext(new ExprContext(_parentctx, _parentState));
						((BinopContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(65);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(66);
						((BinopContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((BinopContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(67);
						((BinopContext)_localctx).rhs = expr(4);
						}
						break;
					case 3:
						{
						_localctx = new BinopContext(new ExprContext(_parentctx, _parentState));
						((BinopContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(68);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(69);
						((BinopContext)_localctx).op = match(AND);
						setState(70);
						((BinopContext)_localctx).rhs = expr(3);
						}
						break;
					case 4:
						{
						_localctx = new BinopContext(new ExprContext(_parentctx, _parentState));
						((BinopContext)_localctx).lhs = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(71);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(72);
						((BinopContext)_localctx).op = match(THEN);
						setState(73);
						((BinopContext)_localctx).rhs = expr(2);
						}
						break;
					case 5:
						{
						_localctx = new RangeContext(new ExprContext(_parentctx, _parentState));
						((RangeContext)_localctx).bottom = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(74);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(75);
						match(TO);
						setState(76);
						((RangeContext)_localctx).top = expr(0);
						setState(78);
						_errHandler.sync(this);
						switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
						case 1:
							{
							setState(77);
							rangeSpec();
							}
							break;
						}
						}
						break;
					}
					} 
				}
				setState(84);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 7:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 1);
		case 4:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36X\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2"+
		"\16\2\27\13\2\3\2\3\2\3\3\3\3\3\4\3\4\5\4\37\n\4\3\5\3\5\3\5\3\5\5\5%"+
		"\n\5\3\5\3\5\5\5)\n\5\5\5+\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t"+
		"\3\t\3\t\5\t9\n\t\3\t\3\t\3\t\3\t\5\t?\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tQ\n\t\7\tS\n\t\f\t\16\tV\13\t"+
		"\3\t\2\3\20\n\2\4\6\b\n\f\16\20\2\7\3\2\23\24\3\2\25\30\3\2\31\32\3\2"+
		"\21\22\3\2\17\20\2]\2\25\3\2\2\2\4\32\3\2\2\2\6\36\3\2\2\2\b*\3\2\2\2"+
		"\n,\3\2\2\2\f\60\3\2\2\2\16\62\3\2\2\2\20>\3\2\2\2\22\24\5\b\5\2\23\22"+
		"\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2\27\25"+
		"\3\2\2\2\30\31\7\2\2\3\31\3\3\2\2\2\32\33\7\13\2\2\33\5\3\2\2\2\34\37"+
		"\7\33\2\2\35\37\7\34\2\2\36\34\3\2\2\2\36\35\3\2\2\2\37\7\3\2\2\2 !\5"+
		"\6\4\2!\"\7\t\2\2\"$\5\20\t\2#%\5\4\3\2$#\3\2\2\2$%\3\2\2\2%+\3\2\2\2"+
		"&(\5\20\t\2\')\5\4\3\2(\'\3\2\2\2()\3\2\2\2)+\3\2\2\2* \3\2\2\2*&\3\2"+
		"\2\2+\t\3\2\2\2,-\7\f\2\2-.\t\2\2\2./\7\r\2\2/\13\3\2\2\2\60\61\t\3\2"+
		"\2\61\r\3\2\2\2\62\63\t\4\2\2\63\17\3\2\2\2\64\65\b\t\1\2\65?\5\6\4\2"+
		"\668\5\16\b\2\679\5\f\7\28\67\3\2\2\289\3\2\2\29?\3\2\2\2:;\7\f\2\2;<"+
		"\5\20\t\2<=\7\r\2\2=?\3\2\2\2>\64\3\2\2\2>\66\3\2\2\2>:\3\2\2\2?T\3\2"+
		"\2\2@A\f\7\2\2AB\t\5\2\2BS\5\20\t\bCD\f\5\2\2DE\t\6\2\2ES\5\20\t\6FG\f"+
		"\4\2\2GH\7\5\2\2HS\5\20\t\5IJ\f\3\2\2JK\7\6\2\2KS\5\20\t\4LM\f\6\2\2M"+
		"N\7\16\2\2NP\5\20\t\2OQ\5\n\6\2PO\3\2\2\2PQ\3\2\2\2QS\3\2\2\2R@\3\2\2"+
		"\2RC\3\2\2\2RF\3\2\2\2RI\3\2\2\2RL\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2"+
		"\2U\21\3\2\2\2VT\3\2\2\2\f\25\36$(*8>PRT";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
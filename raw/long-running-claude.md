# Long-running Claude for scientific computing

**Source:** https://www.anthropic.com/research/long-running-Claude
**Published:** March 23, 2026
**Author:** Siddharth Mishra-Sharma (Researcher, Discovery team, Anthropic)

---

## Overview

This post explains how to apply multi-day agentic coding workflows—including test oracles, persistent memory, and orchestration patterns—to scientific computing tasks outside one's expertise domain.

## The Premise

Scientists traditionally work in conversational loops with AI agents, managing each step closely. As models improved at long-horizon tasks, autonomous workflows became viable. Well-scoped tasks with clear success criteria and occasional oversight fit this model well—such as reimplementing numerical solvers, converting legacy code, or debugging against reference implementations.

Anthropic's C compiler project demonstrated this approach, with Claude working across roughly 2,000 sessions to build a Linux-kernel-capable compiler. This post describes applying similar patterns to scientific computing using Claude Code, with a cosmological Boltzmann solver as the concrete example—implementing a differentiable version to predict Cosmic Microwave Background properties.

## Draft a Plan and Iterate Locally

Invest significant time crafting clear project instructions in a `CLAUDE.md` file at the repository root. Claude treats this file specially, maintaining it in context and referencing it for overall strategy. Critically, Claude can edit these instructions as work progresses, updating them for future sessions when encountering issues.

## Memory Across Sessions

The progress file (`CHANGELOG.md`) serves as the agent's portable long-term memory, functioning as lab notes. Track current status, completed tasks, failed approaches with explanations, accuracy checkpoints, and known limitations. Document failed experiments to prevent successive sessions from repeating dead ends.

## The Test Oracle

Autonomous scientific work requires mechanisms for assessing progress. Use reference implementations, quantifiable objectives, or existing test suites. Instruct agents to expand test coverage and run tests continuously to prevent regressions.

## Git as Coordination

Git provides hands-off progress monitoring and coordination. Agents should commit after meaningful work units, enabling recoverable history and preventing loss if compute allocations expire. Include instructions like: "Run tests before commits. Never commit code breaking existing tests."

## The Execution Loop

After refining plans locally in `CLAUDE.md`, launch a Claude Code session in a terminal multiplexer (tmux) on a compute node. You can detach and check progress periodically—even via phone while waiting in line.

### Example SLURM Job Script

```bash
#!/bin/bash
#SBATCH --job-name=claude-agent
#SBATCH --partition=GPU-shared
#SBATCH --gres=gpu:h100-32:1
#SBATCH --time=48:00:00
#SBATCH --output=agent_%j.log
cd $PROJECT/my-solver
source .venv/bin/activate
export TERM=xterm-256color
tmux new-session -d -s claude "claude; exec bash"
tmux wait-for claude
```

Reattach using: `srun --jobid=JOBID --overlap --pty tmux attach -t claude`

## The Ralph Loop

Models can exhibit "agentic laziness," stopping before completing complex multi-part tasks. The Ralph loop—a for loop that re-prompts when agents claim completion—combats this. Similar patterns include GSD and Claude Code's native `/loop` command.

### Example Invocation

```
/ralph-loop:ralph-loop "Keep working until 0.1% accuracy across entire parameter range" 
--max-iterations 20 --completion-promise "DONE"
```

Claude will iterate up to 20 times until guaranteeing completion with a "DONE" declaration.

## The Result

Claude completed the Boltzmann solver project over several days, achieving sub-percent agreement with the reference CLASS implementation. The development trajectory showed some inefficiencies—initially testing only at single parameter points—but sustained progress toward the 0.1% accuracy target.

The project demonstrated that agent-driven development can compress months or years of research work into days. While not production-grade, it shows significant time compression potential for well-defined scientific tasks.

## Key Insight

As models improve, not running agents feels increasingly costly. With compute access and well-defined success criteria, unused agent-working hours represent abandoned progress opportunities.

## Acknowledgments

Thanks to Eric Kauderer-Abrams for peer review and Xander Balwit, Ethan Dyer, and Rebecca Hiscott for feedback.
